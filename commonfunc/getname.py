# coding:utf-8

'''
Created on 2011-12-8

@author: tongjp
'''

from django.shortcuts import render_to_response
from django.db.models import Q
from django.http import HttpResponse

'''
from management.models import Tcomempl
from oahome.models import ViewEmpl

def autoempllist(request):
    #results = Tcomempl.objects.all()
    #return render_to_response('manaindex.html', {'empllist':results})
    #results = Tcomempl.objects.using('smcodb').all();
    if request.GET.has_key('q'):
        q_str = request.GET['q']
        if len(q_str)>0: #定义输入多少字符后开始查询
            #导入高级查询模式Q 进行逻辑或查询,此处查询结果数最好与JS代码中的限制一致，避免多余开销
            tags = (ViewEmpl.objects.filter(Q (name__icontains=request.GET['q']) | Q (age__icontains=request.GET['q'])))[:10]
            #使用了模型中自定义的属性 full_name
            return HttpResponse('\n'.join(tag.full_name for tag in tags))
    return HttpResponse()
'''