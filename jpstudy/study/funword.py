# coding:utf-8


'''
funword -- 单词操作函数公用单元
Created on 2010-9-2
@author: tongjp

findword() 根据搜素关键词返回查询结果 
pageword() 以分页的形式返回单词查询结果，最多3000条记录
pagenword() 以分页的形式返回生词词查询结果
'''

from django.core.paginator import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db.models import Max,Q


from jpstudy.sysfunc import addtestval
from jpstudy.sysfunc.commfunc import makecode 
from dictdata.models import JaWord,MaxNo,JaGroup

# 查询单词
def findword(vword):
        jwordlist = JaWord.objects.filter(Q(fword=vword)|Q(fpronunciation=vword))     
        if jwordlist:
            return jwordlist
        else:
            return None

# 返回单词列表
def pageword(request):
    results=JaWord.objects.all()[:3000]
    paginator=Paginator(results,10)
    # 确信Request要求是个整数，负责返回1
#    assert False   
    try:
        try:
            page = int(request.POST.get('pageno'))
        except:
            page = int(request.GET.get('page', '1'))
#        if (request.POST.get('pageno')).isdigit():
#            page = int(request.POST.get('pageno', '1'))
#        else:           

    except ValueError:
        page = 1 
    # 如果页码要就超出范围，返回最后一页
    try:
        wordlist = paginator.page(page)
    except (EmptyPage, InvalidPage):
        wordlist = paginator.page(paginator.num_pages)
        
    return wordlist


# 日语单词导入新表
def jaotonew(vword):
    jwordlist = JaWord.objects.exclude(fuser='tongjp')[:500]
    for jword in jwordlist:
        jword.fuser = 'tongjp'
        jword.save()
    return HttpResponseRedirect("/")

# 日语单词导回
def newbackold(vword):
    jwordlist = JaWord.objects.exclude(fuser='tongjp')
    jwordlist.update(fuser='tongjp')
    return HttpResponseRedirect("/")

# 日语单词导入新表
def delwgroup(requst):
    jwgrouplist = JaGroup.objects.all()
    jwgrouplist.delete()  
    return HttpResponseRedirect("/")

# 获取最大单词号
def getmaxno(request):
    results = JaWord.objects.all().order_by('-fwordno')[:1]
    maxno = results.get()
    return HttpResponseRedirect(maxno.fwordno)


