# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-30 00:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpstudy', '0005_auto_20180518_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newword',
            old_name='fjword',
            new_name='fnewword',
        ),
    ]
