from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.cache import cache_page
from django.utils import timezone
from django.conf import settings
from .models import Plant, Photo
import json
from Phidgets.PhidgetException import PhidgetException
from Phidgets.Devices.InterfaceKit import InterfaceKit
# Create your views here.

is_phidget_connected = False
interfaceKit = InterfaceKit()
light_val = 0
try:
    interfaceKit.openRemoteIP('169.254.4.87', 5001, -1, "greenspy")
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
# try:
#     light_val = interfaceKit.getSensorValue(0)
# except PhidgetException as e:
#     print("Phidget Exception %i: %s" % (e.code, e.details))


def main_page(request):
    # Create an interface kit object
    return render(request, 'GreenSpy/index.html')


# def live_page(request):
#     # Create an interface kit object
#     return render(request, 'GreenSpy/live.html')


def json_data(request):
    # Create an interface kit object
    global light_val, temperature_val, humidity_val
    try:
        light_val = interfaceKit.getSensorValue(1)  # Light sensor from input 0
        temperature_val = interfaceKit.getSensorValue(2)  # temperature sensor from input 1
        humidity_val = interfaceKit.getSensorValue(3)  # humidity sensor from input 2
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

    condition_val = [{"Light": light_val, "Temperature": temperature_val, "Humidity": humidity_val}]
    condition_json = json.dumps(condition_val)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(condition_json)
    return response


def power_on(request):
    try:
        interfaceKit.waitForAttach(10000)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        try:
            interfaceKit.closePhidget()
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Exiting....")
            exit(1)
        print("Exiting....")
        exit(1)
    else:
        interfaceKit.setOutputState(0, 1)
    return render(request, 'GreenSpy/powerOn.html')


def power_off(request):
    try:
        interfaceKit.waitForAttach(10000)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        try:
            interfaceKit.closePhidget()
        except PhidgetException as e:
            print("Phidget Exception %i: %s" % (e.code, e.details))
            print("Exiting....")
            exit(1)
        print("Exiting....")
        exit(1)
    else:
        interfaceKit.setOutputState(0, 0)
    return render(request, 'GreenSpy/powerOff.html')


def signup_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return redirect('GreenSpy.views.main_page')
    else:
        signup_form = UserCreationForm()
    return render(request, 'GreenSpy/signup.html', {'signup_form': signup_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('un')
        password = request.POST.get('ps')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # print(request.session.session_key)
            login(request, user)
            # print(request.session.session_key)
            return redirect('GreenSpy.views.main_page')
        elif not request.user.is_authenticated():
            return render(request, 'GreenSpy/errorlogin.html')
    else:
        return render(request, 'GreenSpy/login.html')


def logout_view(request):
    logout(request)
    return redirect('GreenSpy.views.main_page')


###############################################
# Plant list, groups, and detail section       #
###############################################
@cache_page(60 * 15)
@login_required(login_url='/login/')
def plant_detail(request, pk):
    plant_info = get_object_or_404(Plant, pk=pk)
    # plants = Plant.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    # plants_paginator = Paginator(plants, 1)
    next_plant_info = Plant.objects.filter(id__gt=plant_info.id).order_by('id').first()
    prev_plant_info = Plant.objects.filter(id__lt=plant_info.id).order_by('id').last()
    return render(request, 'GreenSpy/plant_detail.html', {'plant_detail': plant_info,
                                                          'plant_detail_next': next_plant_info,
                                                          'plant_detail_prev': prev_plant_info})


@login_required(login_url='/login/')
def plant_list(request):
    photo = Photo.objects.all()
    plants = Plant.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    content = {
        'photos': photo,
        'plants': plants
    }
    return render(request, 'GreenSpy/plant_list.html', content)


@login_required(login_url='/login/')
def contact(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if subject and name and message:
            try:
                send_mail(subject, message, "%s from %s <do_not_replay@domain.com>" % (name, email),
                          [settings.EMAIL_HOST_USER], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Thank you for your message.')
        else:
            return HttpResponse('Please make sure fields are filled and valid.')
    return render(request, 'GreenSpy/contact.html')