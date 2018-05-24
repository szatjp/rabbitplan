# coding:utf-8

'''
Created on 2018.5.23

@author: matsui
'''

import datetime
import urllib.request
import json

from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import requires_csrf_token,csrf_exempt

from commonmd.models import ProCode


def upprocode(request):
    url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/common/recprocode/'
    #url = 'http://127.0.0.1:8000/common/recprocode/'

    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})
    
    if ProCode.objects.filter().exists():
        hdr = {'User-Agent': 'Mozilla/5.0'}
        procodes = serializers.serialize('json',ProCode.objects.filter()).encode(encoding='UTF8')
        req = urllib.request.Request(url,procodes,headers=hdr)  
        response = urllib.request.urlopen(req)
        if response == 'sucess':
            return HttpResponse('sucess')
    #else:

    #html = response.read().decode('utf-8')
    #jsondata = json.loads(html)
    return HttpResponse('sucess')

@csrf_exempt
def recprocode(request):
    if request.method == 'POST':
        #received_json_data = json.loads(request.body).encode(encoding='UTF8')
        
        procodeobjs = serializers.deserialize("json", request.body)
        for procode in procodeobjs:
            if not ProCode.objects.filter(fstateid=procode.object.fstateid).exists():
                procode.object.save()
        
        '''
        for deserialized_object in serializers.deserialize("json", request.POST):
            if deserialized_object:
                deserialized_object.save()
        '''            
    return HttpResponse('sucess')