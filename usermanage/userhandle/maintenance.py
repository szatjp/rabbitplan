# coding:utf-8

'''
Created on 2013-6-21

@author: tong
'''

from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from management.models import employee
from usermanage.models import usertoempl


# 初始化批量导入职员为用户
def EmptoUser(request):
    empllist = employee.objects.all();
    for emplobj in empllist:
        if not User.objects.filter(username=emplobj.fcode).exists():
            user = User.objects.create_user(emplobj.fcode, emplobj.femail, '!QAZ2wsx')
            user.first_name = emplobj.fname
            user.save()
            utoe = usertoempl(
                               fuser = user,
                               femployee = emplobj,
                               flanguage = 'cn'
                               )
            utoe.save()
                           
    return render_to_response('default.html')