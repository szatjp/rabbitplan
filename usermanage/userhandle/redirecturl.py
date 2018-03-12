# coding:utf-8

'''
Created on 2014-10-22

@author: tjp
'''

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from usermanage.models import usertoempl


# 定向用户首页
@login_required
def redirecthome(request):
    userid = request.user.id
    if usertoempl.objects.filter(fuser=userid).exists():
        userempl = usertoempl.objects.get(fuser=userid)
        if userempl.fhomepage:
            return HttpResponseRedirect(userempl.fhomepage)
    else:
        return HttpResponseRedirect('/') 
