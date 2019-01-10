from django.db import models

# Create your models here.


# 数学题表
class MathTest(models.Model):
    fid = models.AutoField(primary_key=True)
    fquestr = models.CharField('问题字符串',max_length=50)
    fnumpara = models.CharField('数字参数',max_length=50)
    fsympara = models.CharField('运算符号参数',max_length=10)
    fanswer = models.CharField('答案',max_length=50)
    fgroup = models.CharField('试题组号',max_length=10)
    fgpnum = models.IntegerField('组内序号')
    fquecla = models.CharField('问题分类',max_length=10)  
    fdate = models.DateTimeField(auto_now=True)