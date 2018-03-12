# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0003_auto_20160119_1655'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cnword',
            unique_together=set([('fword', 'fpronunciation')]),
        ),
        migrations.AlterUniqueTogether(
            name='enword',
            unique_together=set([('fword', 'fpronunciation')]),
        ),
    ]
