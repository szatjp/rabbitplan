# coding:utf-8

'''
Created on 2018.5.23

@author: matsui
'''

import datetime
import urllib.request
import json

from django.http import HttpResponse

from commonfunc.dbtojson import json_encode

from commonmd.models import FreshTime
from dictdata.models import JaWord,EnWord,CnWord,Ja2Cn,Ja2En,En2Cn


# 下载字典
def downfunc(url,dbmodel,freshdate):
    #url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    #url = 'http://127.0.0.1:8000/dict/jpwords/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})

    
    values = {'freshdate' : freshdate}
    
    data = urllib.parse.urlencode(values)
    #data = data.encode('utf8') # data should be bytes
    full_url = url + '?' + data
    req = urllib.request.Request(full_url)    
    #restreq = urllib.request.Request(url) 
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    jsondata = json.loads(html)
    objli = []
    for dictdata in jsondata:
        if dbmodel.objects.filter(pk=dictdata['fwordno']).exists():
            wordobj = dbmodel.objects.get(pk=dictdata['fwordno'])
            wordobj.fword = dictdata['fword']
            wordobj.fpronunciation = dictdata['fpronunciation']
            wordobj.fwordclass = dictdata['fwordclass']
            wordobj.frelaword = dictdata['frelaword']
            wordobj.fuser = dictdata['fuser']
            wordobj.save()              
        else:    
            dictobj = dbmodel(
                fwordno = dictdata['fwordno'],
                fword = dictdata['fword'],
                fpronunciation = dictdata['fpronunciation'],
                fwordclass = dictdata['fwordclass'],
                frelaword = dictdata['frelaword'],
                fuser = dictdata['fuser']          
                )
            objli.append(dictobj)
    if objli:
        dbmodel.objects.bulk_create(objli)
    return 'success'

# 下载互译表
def downtrans(url,trantype,freshdate):
    #url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    #url = 'http://127.0.0.1:8000/dict/jpwords/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})

    
    values = {'freshdate' : freshdate}
    
    data = urllib.parse.urlencode(values)
    #data = data.encode('utf8') # data should be bytes
    full_url = url# + '?' + data
    req = urllib.request.Request(full_url)    
    #restreq = urllib.request.Request(url) 
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    jsondata = json.loads(html)
    objli = []
    if trantype=="ja2cn":
        for dictdata in jsondata:
            if not Ja2Cn.objects.filter(fjaword=dictdata['fjaword'],fcnword=dictdata['fcnword']).exists():    
                jaobj = JaWord.objects.get(pk=dictdata['fjaword'])
                cnobj = CnWord.objects.get(pk=dictdata['fcnword'])
                dictobj = Ja2Cn(
                    fjaword = jaobj,
                    fcnword = cnobj,
                    fuser = dictdata['fuser'],
                    fdate = dictdata['fdate']        
                    )
                objli.append(dictobj)
        if objli:
            Ja2Cn.objects.bulk_create(objli)
    objli = []
    if trantype=="ja2en":
        for dictdata in jsondata:
            if not Ja2En.objects.filter(fjaword=dictdata['fjaword'],fenword=dictdata['fenword']).exists():
                jaobj = JaWord.objects.get(pk=dictdata['fjaword'])
                enobj = EnWord.objects.get(pk=dictdata['fenword'])
                dictobj = Ja2En(
                    fjaword = jaobj,
                    fenword = enobj,
                    fuser = dictdata['fuser'],
                    fdate = dictdata['fdate']        
                    )
                objli.append(dictobj)
        if objli:
            Ja2En.objects.bulk_create(objli)            
    if trantype=="en2cn":
        for dictdata in jsondata:
            if not En2Cn.objects.filter(fenword=dictdata['fenword'],fcnword=dictdata['fcnword']).exists():    
                enobj = EnWord.objects.get(pk=dictdata['fenword'])
                cnobj = CnWord.objects.get(pk=dictdata['fcnword'])
                dictobj = En2Cn(
                    fenword = enobj,
                    fcnword = cnobj,
                    fuser = dictdata['fuser'],
                    fdate = dictdata['fdate']        
                    )
                objli.append(dictobj)
        if objli:
            En2Cn.objects.bulk_create(objli)
    return 'success'

def downdict(request):
    if FreshTime.objects.filter().exists():
        freshdayobj = FreshTime.objects.get()
        freshdate = freshdayobj.ffreshtime-datetime.timedelta(days=1)
    else:
        freshdate = '2018-01-01 00:00:00'
        freshdayobj = FreshTime(
            ffreshtime = freshdate
            )
        freshdayobj.save()
    '''
    # 下载日语字典
    jpurl = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    downfunc(jpurl,JaWord,freshdate)
    # 下载英语字典
    enurl = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/enwords/'
    downfunc(enurl,EnWord,freshdate)    
    # 下载中文字典
    cnurl = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/cnwords/'
    downfunc(cnurl,CnWord,freshdate)    
    
    freshdayobj.ffreshtime = datetime.datetime.now()
    freshdayobj.save()    
  '''
          
    # 日中互译表
    geturl = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/common/jctrans/'
    downtrans(geturl,'ja2cn',freshdate)
    # 日英互译表
    geturl = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/common/jetrans/'
    downtrans(geturl,'ja2en',freshdate)
    # 英中互译表
    geturl = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/common/ectrans/'
    downtrans(geturl,'en2cn',freshdate)        
    #url = 'http://127.0.0.1:8000/dict/jpwords/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})
    return HttpResponse("字典下载成功！")

# 日汉json
def jcjson(request):
    ja2cnobjs = Ja2Cn.objects.values('fjaword','fcnword','fuser','fdate').all()  
    jsondata = json_encode(ja2cnobjs)
    #url = 'http://127.0.0.1:8000/dict/jpwords/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})
    return HttpResponse(jsondata)

# 日汉json
def jejson(request):
    ja2enobjs = Ja2En.objects.values('fjaword','fenword','fuser','fdate').all()  
    jsondata = json_encode(ja2enobjs)
    return HttpResponse(jsondata) 

# 英中json
def ecjson(request):
    en2cnobjs = En2Cn.objects.values('fenword','fcnword','fuser','fdate').all()  
    jsondata = json_encode(en2cnobjs)
    return HttpResponse(jsondata)   
