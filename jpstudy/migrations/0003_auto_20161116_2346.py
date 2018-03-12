# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpstudy', '0002_auto_20161111_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curvegroup',
            name='id',
        ),
        migrations.RemoveField(
            model_name='curveword',
            name='id',
        ),
        migrations.RemoveField(
            model_name='newword',
            name='id',
        ),
        migrations.AddField(
            model_name='curvegroup',
            name='fid',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curveword',
            name='fid',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newword',
            name='fid',
            field=models.IntegerField(default=1, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curvegroup',
            name='fstateid',
            field=models.ForeignKey(to='commonmd.ProCode'),
        ),
        migrations.DeleteModel(
            name='Procode',
        ),
    ]
