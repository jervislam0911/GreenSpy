import os
from django.core.wsgi import get_wsgi_application
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
os.environ['DJANGO_SETTINGS_MODULE'] = 'GreenAutomation.settings'
application = get_wsgi_application()

from GreenSpy.models import Plant
plant_info = get_object_or_404(Plant, pk=8)

next_plant_info = Plant.objects.filter(id__gt=plant_info.id).order_by('id').last()

print next_plant_info
