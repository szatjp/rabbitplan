# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    #path('findword/', searchword),
    #re_path(r'^addnew/(\w+)/$', findtonew),
]

urlpatterns = format_suffix_patterns(urlpatterns)