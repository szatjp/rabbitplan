# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail,EnList,EnDetail

from functest.restful.restfulcall import callrestful

urlpatterns = [
    path('callrestapi/', callrestful)   
]

urlpatterns = format_suffix_patterns(urlpatterns)