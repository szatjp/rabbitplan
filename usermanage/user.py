# coding:utf-8

'''
Created on 2012-3-8

@author: tongjp
'''
import datetime

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.views.generic.list_detail import object_list,object_detail
from django.contrib.auth.models import User
from django.template import RequestContext


# 检验用户是否登录
def userauth(request):
    if request.user.is_authenticated():
        # 登录显示用户个人页面
        return HttpResponseRedirect("/user/person/")
    else:
        # 未登录转向登录页面Do something for anonymous users.
        return HttpResponseRedirect("/accounts/login/")            
    
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")
    
def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/poll/")

'''
def userlist(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "GET":
                return object_list(
                     request,
                     queryset =  User.objects.all(),
                     #template_name = 'pollbase.html',             
                     template_name = 'user/userlist.html',
                     paginate_by = 20,
                     # extra_context = {'srcform': SrcForm}
                )
        else:
            return HttpResponseRedirect("/limit/")
    else:
        return HttpResponseRedirect("/poll/") 
'''       
        
    
# 显示登录用户的个人页面
def personhome(request):
    return HttpResponseRedirect("/user/myhome/")


# 显示用户首页  
def myhome(request):
    return render_to_response("user/userhome.html",context_instance=RequestContext(request))     
        