# coding:utf-8

'''
Created on 2016年1月10日

@author: szxatjp
'''

from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from testapp import views
from testapp.views import SnippetViewSet, UserViewSet

'''
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
'''

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    #url(r'^snippets/$', views.snippet_list),  # 函数方法
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail), # 函数方法
    #url(r'^users/$', views.UserList.as_view(),name='user-list'),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='user-detail'),
    #url(r'^snippets/$', views.SnippetList.as_view(),name='snippet-list'),
    #url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),name='snippet-detail'), 
    #url(r'^$', views.api_root),
    #url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),
    url(r'^', include(router.urls)),   
]

#urlpatterns = format_suffix_patterns(urlpatterns)

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]