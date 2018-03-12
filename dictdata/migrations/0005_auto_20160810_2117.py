# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0004_auto_20160202_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnword',
            name='frelaword',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='enword',
            name='frelaword',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='jaword',
            name='frelaword',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
