# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpstudy', '0003_auto_20161116_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curvegroup',
            name='fid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='curveword',
            name='fid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='newword',
            name='fid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
