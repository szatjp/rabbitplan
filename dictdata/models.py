# coding:utf-8

from django.db import models
from django.template.defaultfilters import default

# Create your models here.


# 单词最大编号
class MaxNo(models.Model):
    flanguage =  models.CharField(max_length=10)
    fmaxno = models.CharField(null=True,max_length=8,blank=True) 
    fdate = models.DateTimeField(auto_now=True)
            
# 日语单词表
class JaWord(models.Model):
    fwordno = models.CharField(primary_key=True,max_length=8)
    fword = models.CharField(max_length=30, blank=True) 
    fpronunciation = models.CharField(null=True, max_length=30, blank=True)
    fwordclass = models.CharField(null=True, max_length=12, blank=True)
    frelaword = models.CharField(null=True, max_length=200, blank=True) 
    fuser = models.CharField(null=True, max_length=30, blank=True)
    fcreater = models.ForeignKey('auth.user', related_name='jaword', on_delete=models.CASCADE) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    class Meta:
        unique_together = ("fword", "fpronunciation")
    
# 中文单词表
class CnWord(models.Model):
    fwordno = models.CharField(primary_key=True,max_length=8)
    fword = models.CharField(max_length=30, blank=True) 
    fpronunciation = models.CharField(null=True, max_length=30, blank=True)
    fwordclass = models.CharField(null=True, max_length=12, blank=True)
    frelaword = models.CharField(null=True, max_length=200, blank=True)  
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    class Meta:
        unique_together = ("fword", "fpronunciation")
    
# 英语单词表
class EnWord(models.Model):
    fwordno = models.CharField(primary_key=True,max_length=8)
    fword = models.CharField(max_length=30, blank=True) 
    fpronunciation = models.CharField(null=True, max_length=30, blank=True)
    fwordclass = models.CharField(null=True, max_length=12, blank=True)
    frelaword = models.CharField(null=True, max_length=200, blank=True)  
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    class Meta:
        unique_together = ("fword", "fpronunciation", "fwordclass")
    
# 日语例句表
class JaSentence(models.Model):
    fsenno = models.CharField(primary_key=True,max_length=8)
    fsentence = models.CharField(null=True, max_length=150, blank=True)
    fcntrans = models.CharField(null=True, max_length=150, blank=True)
    fentrans = models.CharField(null=True, max_length=150, blank=True) 
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    
# 中文例句表
class CnSentence(models.Model):
    fsenno = models.CharField(primary_key=True,max_length=8)
    fsentence = models.CharField(null=True, max_length=150, blank=True)
    fjptrans = models.CharField(null=True, max_length=150, blank=True)
    fentrans = models.CharField(null=True, max_length=150, blank=True) 
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    
# 英文例句表
class EnSentence(models.Model):
    fsenno = models.CharField(primary_key=True,max_length=8)
    fsentence = models.CharField(null=True, max_length=150, blank=True)
    fjptrans = models.CharField(null=True, max_length=150, blank=True)
    fcntrans = models.CharField(null=True, max_length=150, blank=True) 
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    
# 翻译表
class LanTrans(models.Model):
    fid = models.AutoField(primary_key=True)
    fjaword = models.ForeignKey(JaWord)
    fcnword = models.ForeignKey(CnWord)
    fenword = models.ForeignKey(EnWord)
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    
# 日语单词例句
class JaWordSen(models.Model):
    fid = models.AutoField(primary_key=True)
    fword = models.ForeignKey(JaWord)
    fsentence = models.ForeignKey(JaSentence)
    fdate = models.DateTimeField(auto_now=True)
    
# 中文单词例句
class CnWordSen(models.Model):
    fid = models.AutoField(primary_key=True)
    fword = models.ForeignKey(CnWord)
    fsentence = models.ForeignKey(CnSentence)
    fdate = models.DateTimeField(auto_now=True)
    
# 英语单词例句
class EnWordSen(models.Model):
    fid = models.AutoField(primary_key=True)
    fword = models.ForeignKey(EnWord)
    fsentence = models.ForeignKey(EnSentence)
    fdate = models.DateTimeField(auto_now=True)
    
# 单词分类表
class JaGroup(models.Model):
    fjword = models.ForeignKey(JaWord)
    fminclass = models.CharField(max_length=30)
    class Meta:
        db_table = 'Wgroup'