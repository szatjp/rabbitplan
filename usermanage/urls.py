# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns

from usermanage.userhandle.maintenance import Register


urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)