# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-11 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0009_auto_20180330_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jaword',
            name='fcreater',
        ),
    ]