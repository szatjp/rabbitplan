# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from userstudy.words.tagedit import WordClassLi,WordClassCreate,WordClassDetail,WordClassUpdate
from userstudy.words.newwords import searchword,findtonew
from userstudy.words.newwords import NewWordLi

urlpatterns = [
    path('findword/', searchword),
    re_path(r'^addnew/(\w+)/(\w+)/$', findtonew),
    path('newwordli/', NewWordLi.as_view()),
    path('wclass/', WordClassLi.as_view()),
    path('wclass/add/', WordClassCreate.as_view(), name='wclass-add'),
    path('wclass/<slug:pk>/', WordClassDetail.as_view(), name='wclass-detail'), 
    path('wclass/<slug:pk>/update/', WordClassUpdate.as_view(), name='wclass-update'),     
]

urlpatterns = format_suffix_patterns(urlpatterns)