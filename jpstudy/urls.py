# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail
from jpstudy.study import word

urlpatterns = [
    url(r'^findword/$', word.findword),
    url(r'^addnew/(\w+)/$', word.findtonew),
    #url(r'^jpwords/(?P<pk>[a-z0-9]+)/$', JpDetail.as_view()),
    #url(r'^cnwords/$', CnList.as_view()),
    #url(r'^cnwords/(?P<pk>[a-z0-9]+)/$', CnDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)