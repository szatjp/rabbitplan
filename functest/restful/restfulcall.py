# coding=utf-8 

'''
Created on 2018-05-14
@author: matsui
'''

import datetime
import urllib.request
import json

from django.http import HttpResponse

def callrestful(request):
    url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    '''
    data = {"lastdate":"2018-05-14"}
    postData = json.dumps(data)
    postData = bytes(postData,'utf8')
    '''  
    #postData = urllib.parse.urlencode(data).encode('utf-8')
    #restreq = urllib.request.Request(url,postData,{'Content-Type': 'application/json'})
    values = {'name' : 'Michael Foord',
              'location' : 'Northampton',
              'language' : 'Python' }
    
    data = urllib.parse.urlencode(values)
    #data = data.encode('utf8') # data should be bytes
    full_url = url + '?' + data
    req = urllib.request.Request(full_url)    
    #restreq = urllib.request.Request(url) 
    response = urllib.request.urlopen(req)
    html = response.read()
    #jsondata = json.load(html)
    return HttpResponse(html)