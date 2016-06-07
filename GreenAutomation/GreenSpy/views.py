from django.shortcuts import render, HttpResponse
import sys
import json
from Phidgets.PhidgetException import PhidgetException
from Phidgets.Devices.InterfaceKit import InterfaceKit
# Create your views here.
# is_phidget_connected = False
# interfaceKit = InterfaceKit()
# light_val = 0
# try:
#     interfaceKit.openRemoteIP('169.254.4.87', 5001, -1, "greenspy")
# except PhidgetException as e:
#     print("Phidget Exception %i: %s" % (e.code, e.details))
#     print("Exiting....")
# try:
#     light_val = interfaceKit.getSensorValue(0)
# except PhidgetException as e:
#     print("Phidget Exception %i: %s" % (e.code, e.details))


def main_page(request):
    # Create an interface kit object
    return render(request, 'GreenSpy/base.html')


# def json_data(request):
#     # Create an interface kit object
#     global light_val
#     try:
#         light_val = interfaceKit.getSensorValue(0)  # Light sensor from input 0
#     except PhidgetException as e:
#         print("Phidget Exception %i: %s" % (e.code, e.details))
#
#     light_val = [{"Light": light_val}]
#     light_json = json.dumps(light_val)
#     response = HttpResponse()
#     response['Content-Type'] = "text/javascript"
#     response.write(light_json)
#     return response
