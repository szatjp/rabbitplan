# coding:utf-8

'''
Created on 2016-1-18

@author: tjp
'''

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dictdata.dictedit.dataopre import JpList,JpDetail,CnList,CnDetail
from jpstudy.study import word
from commonmd.datatrans.datadown import downdict,jcjson,jejson,ecjson
from commonmd.datatrans.dataup import upprocode,recprocode

urlpatterns = [
    #url(r'^curvecode/$', 'jpstudy.study.learn.curvecode'),  # 设置记忆曲线状态代码
    #url(r'^cclist/$', 'jpstudy.study.learn.curvecodelist'),  # 记忆曲线状态代码列表
    path('downdict/', downdict),  # 下载词典
    path('jctrans/', jcjson),  # 下载Ja2Cn日汉互译
    path('jetrans/', jejson),  # 下载Ja2En日英互译
    path('ectrans/', ecjson),  # 下载EN2Cn英汉互译
    path('improcode/', upprocode),  # 上传记忆曲线状态代码
    path('recprocode/', recprocode),  # 接收记忆曲线状态代码
    #url(r'^jpwords/(?P<pk>[a-z0-9]+)/$', JpDetail.as_view()),
    #url(r'^cnwords/$', CnList.as_view()),
    #url(r'^cnwords/(?P<pk>[a-z0-9]+)/$', CnDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)