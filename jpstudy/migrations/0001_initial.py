# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dictdata', '0005_auto_20160810_2117'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CurveGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fstime', models.DateField()),
                ('fftime', models.DateTimeField(null=True)),
                ('fntime', models.DateTimeField(null=True)),
                ('fgroupnum', models.IntegerField()),
                ('fsmail', models.NullBooleanField()),
                ('ffmail', models.BooleanField(default=False)),
                ('ffmemory', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CurveWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fnumlimit', models.IntegerField(verbose_name=b'\xe6\xaf\x8f\xe7\xbb\x84\xe6\x95\xb0\xe9\x87\x8f')),
                ('fgroupclass', models.CharField(max_length=30)),
                ('fsdate', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xa5\xe6\x9c\x9f')),
                ('fedate', models.DateField(verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('fstime', models.DateField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe8\xae\xb0\xe5\xbf\x86\xe6\x97\xb6\xe9\x97\xb4')),
                ('fmail', models.BooleanField(verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\x8f\x90\xe9\x86\x92')),
                ('fuser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewWord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flevnum', models.IntegerField()),
                ('fcreatedate', models.DateField(auto_now=True)),
                ('fjword', models.ForeignKey(to='dictdata.JaWord')),
                ('fuser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Procode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fstateid', models.IntegerField()),
                ('fstatename', models.CharField(max_length=30)),
                ('fnexttime', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='curvegroup',
            name='fcurveword',
            field=models.ForeignKey(to='jpstudy.CurveWord'),
        ),
        migrations.AddField(
            model_name='curvegroup',
            name='fstateid',
            field=models.ForeignKey(to='jpstudy.Procode'),
        ),
        migrations.AddField(
            model_name='curvegroup',
            name='fuser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
