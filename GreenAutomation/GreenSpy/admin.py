from django.contrib import admin

# Register your models here.
from .models import Plant, Photo

admin.site.register(Plant)
admin.site.register(Photo)