from django.db import models

# Create your models here.


# 数学题表
class MaxNo(models.Model):
    fid = models.AutoField(primary_key=True)
    fnumpara = models.CharField(max_length=50)
    fsympara = models.CharField(max_length=10)
    fgroup = models.CharField('试题组号',max_length=10)
    fgpnum = models.IntegerField('组内序号')  
    fdate = models.DateTimeField(auto_now=True)