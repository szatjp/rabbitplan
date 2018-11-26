# coding:utf-8

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from dictdata.models import JaWord
from commonmd.models import CurveGroup
    
    
# 生词表
class JpNewWord(models.Model):
    fid = models.AutoField(primary_key=True)
    fnewword = models.ForeignKey(JaWord,on_delete=models.CASCADE)
    fuser = models.ForeignKey(User,on_delete=models.CASCADE)
    flevnum = models.IntegerField(null=True)
    fcurvegroup = models.ForeignKey(CurveGroup,on_delete=models.CASCADE,null=True,verbose_name="生词组") # 关联到单词组使用的选取条件
    fgroupnum = models.CharField(null=True,max_length=20,verbose_name="组号")
    fcreatedate = models.DateField(auto_now=True)

