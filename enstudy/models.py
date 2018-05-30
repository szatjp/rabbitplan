# coding utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from dictdata.models import EnWord
from commonmd.models import ProCode


# 生词表
class NewWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnewword = models.ForeignKey(EnWord,related_name="enword2new")
    fuser = models.ForeignKey(User,related_name="newword2user")
    fgroupnum = models.IntegerField(null=True,verbose_name="组号")
    flevnum = models.IntegerField()
    fcreatedate = models.DateField(auto_now=True)

    
# 单词组选取条件
class CurveWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnumlimit = models.IntegerField(verbose_name="每组数量")
    fgroupclass = models.CharField(max_length=30)
    fuser = models.ForeignKey(User,related_name="encurvew2user")    
    fstime = models.CharField("默认开始时间", max_length=5, null=True) #开始记忆时间    
    fmail = models.BooleanField(verbose_name="邮件提醒") #是否需要发送Email提醒
    
# 单词组和进度
class CurveGroup(models.Model):
    fid = models.AutoField(primary_key=True)
    fcurveword = models.ForeignKey(CurveWord,related_name="enword2curve") # 关联到单词组使用的选取条件
    fstateid = models.ForeignKey(ProCode,related_name="enword2procode")
    fuser = models.ForeignKey(User,related_name="encurveg2user") # 用户
    fstime = models.DateTimeField() # 预订开始记忆日期
    fftime = models.DateTimeField(null=True) # 记忆完成时间
    fntime = models.DateTimeField(null=True) # 下次记忆时间
    fgroupnum = models.IntegerField(verbose_name="组号")
    fsmail =models.NullBooleanField() # 是否需要发送Email提醒
    ffmail = models.BooleanField(default = False) # 是否完成Email通知
    ffmemory = models.NullBooleanField() # 是否完成记忆过程  