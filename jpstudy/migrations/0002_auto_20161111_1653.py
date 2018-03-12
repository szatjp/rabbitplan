# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpstudy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curvegroup',
            name='fstateid',
            field=models.ForeignKey(to='jpstudy.ProCode'),
        ),
    ]
