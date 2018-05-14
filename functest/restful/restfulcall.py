# coding=utf-8 

'''
Created on 2018-05-14
@author: matsui
'''

import datetime
import urllib.request
import json

def callrestful(request):
    url = 'http://django-psql-persistent-rabbitplan.193b.starter-ca-central-1.openshiftapps.com/dict/jpwords/'
    data = {"lastdate":"2018-05-14"}
    postData = urllib.parse.urlencode(data).encode()     
    response = urllib.request.urlopen(url,postData)
    html = response.read()
    jsondata = json.load(html)
    return jsondata