# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail
from userstudy.words.newwords import searchword,findtonew
from userstudy.words.newwords import NewWordLi

urlpatterns = [
    path('findword/', searchword),
    re_path(r'^addnew/(\w+)/(\w+)/$', findtonew),
    path('newwordli/', NewWordLi),
]

urlpatterns = format_suffix_patterns(urlpatterns)