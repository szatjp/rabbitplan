# coding:utf-8

from django.db import models

from django.contrib.auth.models import User

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
    
# 生词组和进度
class CurveGroup(models.Model):
    fid = models.AutoField(primary_key=True)
    fgroupnum = models.CharField(null=True,max_length=20,verbose_name="组号")
    #fcurveword = models.ForeignKey(CurveWord,on_delete=models.CASCADE) # 关联到单词组使用的选取条件
    fstateid = models.ForeignKey(ProCode,on_delete=models.CASCADE) # 单词组进度代码
#    fstateid = ndb.IntegerProperty(required=True)
    fuser = models.ForeignKey(User,on_delete=models.CASCADE) # 用户
    fstime = models.DateField() # 预订开始记忆日期
    fftime = models.DateTimeField(null=True) # 记忆完成时间
    fntime = models.DateTimeField(null=True) # 下次记忆时间
    fsmail =models.NullBooleanField() # 是否需要发送Email提醒
    ffmail = models.BooleanField(default = False) # 是否完成Email通知
    ffmemory = models.NullBooleanField() # 是否完成记忆过程 
        
# 单词组选取条件
class CurveWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnumlimit = models.IntegerField(verbose_name="每组数量")
    fgroupclass = models.CharField(max_length=30,verbose_name="条件标识")
    #fuser = models.ForeignKey(User,on_delete=models.CASCADE)
    #fsdate = models.DateField(verbose_name="开始日期") #选取范围起始日期
    #fedate = models.DateField(verbose_name="结束日期") #选取范围结束日期
    fstime = models.DateField(verbose_name="开始记忆时间") #开始记忆时间    
    fmail = models.BooleanField(verbose_name="邮件提醒") #是否需要发送Email提醒 
