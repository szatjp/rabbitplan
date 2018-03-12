# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from jpstudy.study import word

urlpatterns = [
    url(r'^findword/$', word.findword),
    url(r'^addnew/(\w+)/$', word.findtonew), 
]

urlpatterns = format_suffix_patterns(urlpatterns)