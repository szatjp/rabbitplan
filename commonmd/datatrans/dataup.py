# coding:utf-8

'''
Created on 2018.5.23

@author: matsui
'''

import datetime
import urllib.request
import json

from django.http import HttpResponse

from commonmd.models import ProCode


def upprocode(request):
    url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    #url = 'http://127.0.0.1:8000/dict/jpwords/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})
    
    if ProCode.objects.filter().exists():
        freshdate = ProCode.objects.filter()
    else:
        freshdate = '2018-05-15 00:00:00'
    
    values = {'freshdate' : freshdate}
    
    data = urllib.parse.urlencode(values)
    #data = data.encode('utf8') # data should be bytes
    full_url = url + '?' + data
    req = urllib.request.Request(full_url)    
    #restreq = urllib.request.Request(url) 
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    jsondata = json.loads(html)
    return HttpResponse(html)