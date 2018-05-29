# coding:utf-8

'''
Created on 2018.5.23

@author: matsui
'''

import datetime
import urllib.request
import json

from django.http import HttpResponse

from commonmd.models import FreshTime
from dictdata.models import JaWord


def downdict(request):
    url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    #url = 'http://127.0.0.1:8000/dict/jpwords/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})
    
    if FreshTime.objects.filter().exists():
        freshdayobj = FreshTime.objects.get()
        freshdate = freshdayobj.ffreshtime-datetime.timedelta(days=1)
    else:
        freshdate = '2018-01-01 00:00:00'
        freshdayobj = FreshTime(
            ffreshtime = freshdate
            )
        freshdayobj.save()
    
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
        if JaWord.objects.filter(pk=dictdata['fwordno']).exists():
            wordobj = JaWord.objects.get(pk=dictdata['fwordno'])
            wordobj.fword = dictdata['fword']
            wordobj.fpronunciation = dictdata['fpronunciation']
            wordobj.fwordclass = dictdata['fwordclass']
            wordobj.frelaword = dictdata['frelaword']
            wordobj.fuser = dictdata['fuser']
            wordobj.save()              
        else:    
            dictobj = JaWord(
                fwordno = dictdata['fwordno'],
                fword = dictdata['fword'],
                fpronunciation = dictdata['fpronunciation'],
                fwordclass = dictdata['fwordclass'],
                frelaword = dictdata['frelaword'],
                fuser = dictdata['fuser']          
                )
            objli.append(dictobj)
    JaWord.objects.bulk_create(objli)
    freshdayobj.ffreshtime = datetime.datetime.now()
    freshdayobj.save()
    return HttpResponse(html)