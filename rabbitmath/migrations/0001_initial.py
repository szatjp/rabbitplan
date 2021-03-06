# Generated by Django 2.0.9 on 2019-01-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MathTest',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('fquestr', models.CharField(max_length=50, verbose_name='问题字符串')),
                ('fnumpara', models.CharField(max_length=50, verbose_name='数字参数')),
                ('fsympara', models.CharField(max_length=10, verbose_name='运算符号参数')),
                ('fanswer', models.CharField(max_length=50, verbose_name='答案')),
                ('fgroup', models.CharField(max_length=10, verbose_name='试题组号')),
                ('fgpnum', models.IntegerField(verbose_name='组内序号')),
                ('fquecla', models.CharField(max_length=10, verbose_name='问题分类')),
                ('fdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
