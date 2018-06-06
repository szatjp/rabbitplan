# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictdata', '0006_jagroup_maxno'),
    ]

    operations = [
        migrations.AddField(
            model_name='jaword',
            name='fcreater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jaword', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
