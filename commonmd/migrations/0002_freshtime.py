# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-18 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonmd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreshTime',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('ffreshtime', models.DateTimeField()),
                ('fuser', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
