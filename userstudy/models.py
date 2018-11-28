from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from dictdata.models import JaWord,CnWord,EnWord
from commonmd.models import CurveGroup
    
    
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