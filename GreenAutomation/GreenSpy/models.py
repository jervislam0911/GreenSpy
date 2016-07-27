from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

FAMILY_CATEGORY = (('Araceae', 'Araceae'),
                   ('Begonia', 'Begonia'),
                   ('Cactus', 'Cactus'),
                   ('Dacrymycetes', 'Dacrymycetes'),
                   ('Nymphaeaceae', 'Nymphaeaceae'),
                   ('Rutaceae', 'Rutaceae'))


# Create Plant models here.
class Plant(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=100, choices=FAMILY_CATEGORY, default='Araceae')
    description = models.TextField(max_length=600)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    light_intensity = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.name


# Create Photo models here.
class Photo(models.Model):
    plant = models.ForeignKey(Plant)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo')
    caption = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
