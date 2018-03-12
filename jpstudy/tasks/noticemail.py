# coding: utf-8 
'''
Created on 2011-6-7

@author: tongjp
'''
import datetime
from django.http import HttpResponse

from jxuexi.sysfunc.addtestval import addval

def memmail(request):
    # 取得需要发送邮件的列表
    #addval('邮件cron','成功')
    return HttpResponse("ok")
             
            
