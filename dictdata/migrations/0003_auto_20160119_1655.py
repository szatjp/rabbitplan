# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0002_auto_20160118_1036'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='jaword',
            unique_together=set([('fword', 'fpronunciation')]),
        ),
    ]
