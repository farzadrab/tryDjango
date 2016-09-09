# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default=b'my job', max_length=1200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=b'my location', max_length=1200),
        ),
    ]
