# coding:utf-8

from django.db import models

# Create your models here.



# 记忆曲线进度代码表
class ProCode(models.Model):
    fstateid = models.CharField(primary_key=True,max_length=3)
    fstatename =  models.CharField(max_length=30)
    fnexttime = models.IntegerField()
    
# 词库更新时间表
class FreshTime(models.Model):
    fid =  models.AutoField(primary_key=True)   
    ffreshtime = models.DateTimeField()
    fuser = models.CharField(null=True, max_length=30, blank=True) 
