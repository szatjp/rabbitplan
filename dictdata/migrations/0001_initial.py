# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CnSentence',
            fields=[
                ('fsenno', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('fsentence', models.CharField(max_length=150, null=True, blank=True)),
                ('fjptrans', models.CharField(max_length=150, null=True, blank=True)),
                ('fentrans', models.CharField(max_length=150, null=True, blank=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('favail', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CnWord',
            fields=[
                ('fwordno', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('fword', models.CharField(max_length=30, blank=True)),
                ('fpronunciation', models.CharField(max_length=30, null=True, blank=True)),
                ('fwordclass', models.CharField(max_length=30, null=True, blank=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('favail', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CnWordSen',
            fields=[
                ('fid', models.AutoField(serialize=False, primary_key=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('fsentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.CnSentence')),
                ('fword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.CnWord')),
            ],
        ),
        migrations.CreateModel(
            name='EnSentence',
            fields=[
                ('fsenno', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('fsentence', models.CharField(max_length=150, null=True, blank=True)),
                ('fjptrans', models.CharField(max_length=150, null=True, blank=True)),
                ('fcntrans', models.CharField(max_length=150, null=True, blank=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('favail', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnWord',
            fields=[
                ('fwordno', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('fword', models.CharField(max_length=30, blank=True)),
                ('fpronunciation', models.CharField(max_length=30, null=True, blank=True)),
                ('fwordclass', models.CharField(max_length=30, null=True, blank=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('favail', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnWordSen',
            fields=[
                ('fid', models.AutoField(serialize=False, primary_key=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('fsentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.EnSentence')),
                ('fword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.EnWord')),
            ],
        ),
        migrations.CreateModel(
            name='JaSentence',
            fields=[
                ('fsenno', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('fsentence', models.CharField(max_length=150, null=True, blank=True)),
                ('fcntrans', models.CharField(max_length=150, null=True, blank=True)),
                ('fentrans', models.CharField(max_length=150, null=True, blank=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('favail', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JaWord',
            fields=[
                ('fwordno', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('fword', models.CharField(max_length=30, blank=True)),
                ('fpronunciation', models.CharField(max_length=30, null=True, blank=True)),
                ('fwordclass', models.CharField(max_length=30, null=True, blank=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('favail', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JaWordSen',
            fields=[
                ('fid', models.AutoField(serialize=False, primary_key=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('fsentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.JaSentence')),
                ('fword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.JaWord')),
            ],
        ),
        migrations.CreateModel(
            name='LanTrans',
            fields=[
                ('fid', models.AutoField(serialize=False, primary_key=True)),
                ('fuser', models.CharField(max_length=30, null=True, blank=True)),
                ('fdate', models.DateTimeField(auto_now=True)),
                ('fcnword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.CnWord')),
                ('fenword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.EnWord')),
                ('fjaword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.JaWord')),
            ],
        ),
    ]
