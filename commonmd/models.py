# coding:utf-8

from django.db import models

# Create your models here.



# 记忆曲线进度代码表
class ProCode(models.Model):
    fstateid = models.IntegerField(primary_key=True)
    fstatename =  models.CharField(max_length=30)
    fnexttime = models.IntegerField()