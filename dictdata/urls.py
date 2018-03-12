# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail,EnList,EnDetail

urlpatterns = [
    url(r'^jpwords/$', JpList.as_view()),
    url(r'^jpwords/(?P<pk>[a-z0-9]+)/$', JpDetail.as_view()),
    url(r'^cnwords/$', CnList.as_view()),
    url(r'^cnwords/(?P<pk>[a-z0-9]+)/$', CnDetail.as_view()),
    url(r'^enwords/$', EnList.as_view()),
    url(r'^enwords/(?P<pk>[a-z0-9]+)/$', EnDetail.as_view()),         
]

urlpatterns = format_suffix_patterns(urlpatterns)