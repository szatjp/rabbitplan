# Generated by Django 2.0.9 on 2018-11-28 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jpstudy', '0008_auto_20181126_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jpnewword',
            name='fcurvegroup',
        ),
        migrations.RemoveField(
            model_name='jpnewword',
            name='fnewword',
        ),
        migrations.RemoveField(
            model_name='jpnewword',
            name='fuser',
        ),
        migrations.DeleteModel(
            name='JpNewWord',
        ),
    ]