# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-18 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpstudy', '0004_auto_20161130_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curveword',
            name='fedate',
            field=models.DateField(verbose_name='结束日期'),
        ),
        migrations.AlterField(
            model_name='curveword',
            name='fmail',
            field=models.BooleanField(verbose_name='邮件提醒'),
        ),
        migrations.AlterField(
            model_name='curveword',
            name='fnumlimit',
            field=models.IntegerField(verbose_name='每组数量'),
        ),
        migrations.AlterField(
            model_name='curveword',
            name='fsdate',
            field=models.DateField(verbose_name='开始日期'),
        ),
        migrations.AlterField(
            model_name='curveword',
            name='fstime',
            field=models.DateField(verbose_name='开始记忆时间'),
        ),
    ]
