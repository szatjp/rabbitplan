# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail
from jpstudy.study import word

urlpatterns = [
    path(r'^findword/$', word.findword),
    path(r'^addnew/(\w+)/$', word.findtonew),
    #url(r'^jpwords/(?P<pk>[a-z0-9]+)/$', JpDetail.as_view()),
    #url(r'^cnwords/$', CnList.as_view()),
    #url(r'^cnwords/(?P<pk>[a-z0-9]+)/$', CnDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)