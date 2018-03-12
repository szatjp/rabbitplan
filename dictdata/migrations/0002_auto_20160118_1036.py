# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnsentence',
            name='favail',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='cnword',
            name='favail',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='ensentence',
            name='favail',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='enword',
            name='favail',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='jasentence',
            name='favail',
            field=models.CharField(default=b'1', max_length=1),
        ),
        migrations.AlterField(
            model_name='jaword',
            name='favail',
            field=models.CharField(default=b'1', max_length=1),
        ),
    ]
