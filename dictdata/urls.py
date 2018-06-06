# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail,EnList,EnDetail

urlpatterns = [
    path('jpwords/', JpList.as_view()),
    re_path(r'^jpwords/(?P<pk>[a-z0-9]+)/$', JpDetail.as_view()),
    path('cnwords/', CnList.as_view()),
    re_path(r'^cnwords/(?P<pk>[a-z0-9]+)/$', CnDetail.as_view()),
    path('enwords/', EnList.as_view()),
    re_path(r'^enwords/(?P<pk>[a-z0-9]+)/$', EnDetail.as_view()),         
]

urlpatterns = format_suffix_patterns(urlpatterns)