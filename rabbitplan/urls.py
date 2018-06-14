# coding:utf-8

from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout

from rest_framework import serializers, viewsets, routers

from welcome.views import index, health

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('', index),
    #path('^', include(router.urls)),
    path('health', health),
    path('admin/', admin.site.urls),
    #path('community/', include('aggregator.urls')),
    path('dict/', include('dictdata.urls')),   # 字典应用
    path('functest/', include('functest.urls')),   # 功能测试
    path('jp/', include('jpstudy.urls')),   # 日语学习
    path('common/', include('commonmd.urls')),   # 共通模块
]

urlpatterns += [
    path('login', login, name='login'),
]

urlpatterns += [
    path('api-auth', include('rest_framework.urls',
                               namespace='rest_framework')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
