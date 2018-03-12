# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0005_auto_20160810_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='JaGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fminclass', models.CharField(max_length=30)),
                ('fjword', models.ForeignKey(to='dictdata.JaWord')),
            ],
            options={
                'db_table': 'Wgroup',
            },
        ),
        migrations.CreateModel(
            name='MaxNo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flanguage', models.CharField(max_length=10)),
                ('fmaxno', models.CharField(max_length=8, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
