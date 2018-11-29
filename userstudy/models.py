from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from dictdata.models import JaWord,CnWord,EnWord
from commonmd.models import CurveGroup
from django.template.defaultfilters import default
    
    
# 日文生词表
class JpNewWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnewword = models.ForeignKey(JaWord,on_delete=models.CASCADE)
    fuser = models.ForeignKey(User,on_delete=models.CASCADE)
    flevnum = models.IntegerField(null=True)
    fgroupnum = models.CharField(null=True,max_length=20,verbose_name="组号")
    fcreatedate = models.DateField(auto_now=True)
    
# 中文生词表
class CnNewWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnewword = models.ForeignKey(CnWord,on_delete=models.CASCADE)
    fuser = models.ForeignKey(User,on_delete=models.CASCADE)
    flevnum = models.IntegerField(null=True)
    fgroupnum = models.CharField(null=True,max_length=20,verbose_name="组号")
    fcreatedate = models.DateField(auto_now=True)
    
# 英文文生词表
class EnNewWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnewword = models.ForeignKey(EnWord,on_delete=models.CASCADE)
    fuser = models.ForeignKey(User,on_delete=models.CASCADE)
    flevnum = models.IntegerField(null=True)
    fgroupnum = models.CharField(null=True,max_length=20,verbose_name="组号")
    fcreatedate = models.DateField(auto_now=True)
    
class WordClass(models.Model):
    fid = models.AutoField(primary_key=True)
    fclassname = models.CharField(max_length=50,verbose_name="标签名称")
    fopen = models.CharField(max_length=1,default='0') # 默认不对外开放
    fuser = models.ForeignKey(User,on_delete=models.CASCADE)
    fcreatedate = models.DateField(auto_now=True)
    class Meta:
        unique_together = ('fuser','fclassname')
        
# 日语单词分类表
class JaGroup(models.Model):
    fjword = models.ForeignKey(JaWord,on_delete=models.CASCADE)
    fwordclass = models.ForeignKey(WordClass,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('fjword','fwordclass')    
        
# 英语单词分类表
class EnGroup(models.Model):
    feword = models.ForeignKey(EnWord,on_delete=models.CASCADE)
    fwordclass = models.ForeignKey(WordClass,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('feword','fwordclass')    
        
# 汉语单词分类表
class CnGroup(models.Model):
    fcword = models.ForeignKey(CnWord,on_delete=models.CASCADE)
    fwordclass = models.ForeignKey(WordClass,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('fcword','fwordclass')    