# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0007_jaword_fcreater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnword',
            name='fwordclass',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='enword',
            name='fwordclass',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jaword',
            name='fwordclass',
            field=models.CharField(max_length=12, null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='enword',
            unique_together=set([('fword', 'fpronunciation', 'fwordclass')]),
        ),
    ]
