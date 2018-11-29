# coding:utf-8

from django.db import models
from django.template.defaultfilters import default
from django.urls import reverse

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
    frelaword = models.CharField(null=True, max_length=100, blank=True) 
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    class Meta:
        unique_together = ("fword", "fpronunciation")
    def get_absolute_url(self):
        return reverse('jaword-detail', args=[self.fwordno])         
    
# 中文单词表
class CnWord(models.Model):
    fwordno = models.CharField(primary_key=True,max_length=8)
    fword = models.CharField(max_length=30, blank=True) 
    fpronunciation = models.CharField(null=True, max_length=30, blank=True)
    fwordclass = models.CharField(null=True, max_length=12, blank=True)
    frelaword = models.CharField(null=True, max_length=100, blank=True)  
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    class Meta:
        unique_together = ("fword", "fpronunciation")
    def get_absolute_url(self):
        return reverse('cnword-detail', args=[self.fwordno])           
       
    
# 英语单词表
class EnWord(models.Model):
    fwordno = models.CharField(primary_key=True,max_length=8)
    fword = models.CharField(max_length=30, blank=True) 
    fpronunciation = models.CharField(null=True, max_length=30, blank=True)
    fwordclass = models.CharField(null=True, max_length=12, blank=True)
    frelaword = models.CharField(null=True, max_length=100, blank=True)  
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    favail = models.CharField(max_length=1,default='1')
    class Meta:
        unique_together = ("fword", "fpronunciation", "fwordclass")
    def get_absolute_url(self):
        return reverse('enword-detail', args=[self.fwordno])        
    
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
    
# 日文汉语互译表
class Ja2Cn(models.Model):
    fid = models.AutoField(primary_key=True)
    fjaword = models.ForeignKey(JaWord,on_delete=models.CASCADE,)
    fcnword = models.ForeignKey(CnWord,on_delete=models.CASCADE,)
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("fjaword", "fcnword")    
    
# 日文英语互译表
class Ja2En(models.Model):
    fid = models.AutoField(primary_key=True)
    fjaword = models.ForeignKey(JaWord,on_delete=models.CASCADE)
    fenword = models.ForeignKey(EnWord,on_delete=models.CASCADE)
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("fjaword", "fenword")        
    
# 英语汉语互译表
class En2Cn(models.Model):
    fid = models.AutoField(primary_key=True)
    fenword = models.ForeignKey(EnWord,on_delete=models.CASCADE)
    fcnword = models.ForeignKey(CnWord,on_delete=models.CASCADE)
    fuser = models.CharField(null=True, max_length=30, blank=True) 
    fdate = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("fenword", "fcnword")                
    
# 日语单词例句
class JaWordSen(models.Model):
    fid = models.AutoField(primary_key=True)
    fword = models.ForeignKey(JaWord,on_delete=models.CASCADE)
    fsentence = models.ForeignKey(JaSentence,on_delete=models.CASCADE)
    fdate = models.DateTimeField(auto_now=True)
    
# 中文单词例句
class CnWordSen(models.Model):
    fid = models.AutoField(primary_key=True)
    fword = models.ForeignKey(CnWord,on_delete=models.CASCADE)
    fsentence = models.ForeignKey(CnSentence,on_delete=models.CASCADE)
    fdate = models.DateTimeField(auto_now=True)
    
# 英语单词例句
class EnWordSen(models.Model):
    fid = models.AutoField(primary_key=True)
    fword = models.ForeignKey(EnWord,on_delete=models.CASCADE)
    fsentence = models.ForeignKey(EnSentence,on_delete=models.CASCADE)
    fdate = models.DateTimeField(auto_now=True)
    