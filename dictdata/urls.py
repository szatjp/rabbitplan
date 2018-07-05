# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns

from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail,EnList,EnDetail
from dictdata.cndict.cnmaintain import CnWordLi,CnWordCreate,CnWordDetail,CnWordUpdate
from dictdata.jpdict.jamaintain import JaWordLi,JaWordCreate,JaWordDetail,JaWordUpdate

urlpatterns = [
    path('jpwords/', JpList.as_view()),
    re_path(r'^jpwords/(?P<pk>[a-z0-9]+)/$', JpDetail.as_view()),
    path('cnwords/', CnList.as_view()),
    re_path(r'^cnwords/(?P<pk>[a-z0-9]+)/$', CnDetail.as_view()),
    path('enwords/', EnList.as_view()),
    re_path(r'^enwords/(?P<pk>[a-z0-9]+)/$', EnDetail.as_view()),
    path('cnword/', CnWordLi.as_view()),
    path('cnword/add/', CnWordCreate.as_view(), name='cnword-add'),
    path('cnword/<slug:pk>/', CnWordDetail.as_view(), name='cnword-detail'),
    path('cnword/<slug:pk>/update/', CnWordUpdate.as_view(), name='cnword-update'),
    #path('cnword/<int:pk>/delete/', CnWordDelete.as_view(), name='cnword-delete'),
    path('jaword/', JaWordLi.as_view()),
    path('jaword/add/', JaWordCreate.as_view(), name='jaword-add'),
    path('jaword/<slug:pk>/', JaWordDetail.as_view(), name='jaword-detail'), 
    path('jaword/<slug:pk>/update/', JaWordUpdate.as_view(), name='jaword-update'),             
]

urlpatterns = format_suffix_patterns(urlpatterns)