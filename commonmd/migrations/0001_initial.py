# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProCode',
            fields=[
                ('fstateid', models.IntegerField(serialize=False, primary_key=True)),
                ('fstatename', models.CharField(max_length=30)),
                ('fnexttime', models.IntegerField()),
            ],
        ),
    ]
