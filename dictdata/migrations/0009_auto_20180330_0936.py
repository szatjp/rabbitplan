# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0008_auto_20161209_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnsentence',
            name='favail',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='cnword',
            name='favail',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='ensentence',
            name='favail',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='enword',
            name='favail',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='jasentence',
            name='favail',
            field=models.CharField(default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='jaword',
            name='favail',
            field=models.CharField(default='1', max_length=1),
        ),
    ]
