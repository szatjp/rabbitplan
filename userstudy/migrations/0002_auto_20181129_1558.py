# Generated by Django 2.0.9 on 2018-11-29 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictdata', '0014_auto_20181129_1551'),
        ('userstudy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CnGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fcword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.CnWord')),
            ],
        ),
        migrations.CreateModel(
            name='EnGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.EnWord')),
            ],
        ),
        migrations.CreateModel(
            name='JaGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fjword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictdata.JaWord')),
            ],
        ),
        migrations.CreateModel(
            name='WordClass',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('fclassname', models.CharField(max_length=50, verbose_name='标签名称')),
                ('fopen', models.CharField(default='0', max_length=1)),
                ('fcreatedate', models.DateField(auto_now=True)),
                ('fuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jagroup',
            name='fwordclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userstudy.WordClass'),
        ),
        migrations.AddField(
            model_name='engroup',
            name='fwordclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userstudy.WordClass'),
        ),
        migrations.AddField(
            model_name='cngroup',
            name='fwordclass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userstudy.WordClass'),
        ),
        migrations.AlterUniqueTogether(
            name='wordclass',
            unique_together={('fuser', 'fclassname')},
        ),
        migrations.AlterUniqueTogether(
            name='jagroup',
            unique_together={('fjword', 'fwordclass')},
        ),
        migrations.AlterUniqueTogether(
            name='engroup',
            unique_together={('feword', 'fwordclass')},
        ),
        migrations.AlterUniqueTogether(
            name='cngroup',
            unique_together={('fcword', 'fwordclass')},
        ),
    ]
