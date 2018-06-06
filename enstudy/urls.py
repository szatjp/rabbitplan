# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from jpstudy.study import word

urlpatterns = [
    path(r'^findword/$', word.findword),
    path(r'^addnew/(\w+)/$', word.findtonew), 
]

urlpatterns = format_suffix_patterns(urlpatterns)