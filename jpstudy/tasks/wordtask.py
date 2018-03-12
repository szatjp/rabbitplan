# coding:utf-8

'''
Created on 2012-7-10

@author: tong
'''

import datetime

from django.http import HttpResponse
from jxuexi.models import CurveGroup,Nword

# 清除已经完成的记忆组
def cleangroup(request):
    # 取得已经记忆完成的单词组
    result = CurveGroup.objects.filter(ffmemory=True,fftime__lte=datetime.date.today()-datetime.timedelta(days=3))
    result.filter('ffmemory = ', True).filter('fftime < ',datetime.date.today()-datetime.timedelta(days=3))
    for memgroup in result:
        #curgroup = memgroup.key
        results = Nword.objects.filter(fdate__gte=memgroup.fcurveword.fsdate,fdate__lte=memgroup.fcurveword.fedat)
        wordlist = results.fetch(memgroup.fcurveword.fnumlimit,offset=memgroup.fcurveword.fnumlimit*(memgroup.fgroupnum-1))
        wordlist.delete()
    result.delete()
        
    return HttpResponse(status=240)  