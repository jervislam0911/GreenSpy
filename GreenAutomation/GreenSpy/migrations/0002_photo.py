# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-11 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GreenSpy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photo')),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GreenSpy.Plant')),
            ],
        ),
    ]
