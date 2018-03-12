# coding:utf-8

'''
Created on 2014-4-18

@author: jessie
'''

import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import *
from django.http import HttpResponseRedirect

from jpstudy.models import CurveGroup, CurveWord, NewWord
from commonmd.models import ProCode
from jpstudy.forms import CurveSel, ProcodeForm

# 打开记忆曲线法主页面
def curvemain(request):
    if request.method == "GET":
        curuser = request.user
#        results = models.CruveGroup.all()
#        results = results.filter('fuser=', curuser) 
        results = CurveGroup.objects.filter(fuser=curuser)
        cglist = results[:100]
            #addtestval.addval('resultcount', str(results.count()))
        return render_to_response('person/curve.html',{'wglist':cglist,'userinfo':curuser},context_instance=RequestContext(request))
    
# 增加记忆曲线词组设定
def curveadd(request):
    if request.method == "GET":
        form = CurveSel
        return render_to_response('jword/newcurve.html',{'curvesel':form},context_instance=RequestContext(request))
    if request.method == "POST":
#        curuser=request.session.get('username', None),
        form =  CurveSel(request.POST)
        if form.is_valid():
            curverec = form.save(commit=False)
            curverec.fuser = request.user
            curverec.fgroupclass = 'newword'                
            curverec.save()
            
        sprocode = ProCode.objects.get(fstateid=0)
        results=NewWord.objects.filter(fuser=request.user,fdate__gte=curverec.fsdate,fdate__lte=curverec.fedate)
        recsum=results.count()
        groupnum=int(ceil(recsum*1.0/curverec.fnumlimit))

        while groupnum>0:
            cruvegrp=CurveGroup(
              fcurveword = curverec,
              fgroupnum = groupnum,
              fstateid = sprocode,
              fstime = curverec.fstime+datetime.timedelta(days=(groupnum-1)*3),               
              fuser = curverec.fuser,
              fsmail = curverec.fmail
            )
#            assert False
            cruvegrp.save()
            groupnum = groupnum-1            
            
    return render_to_response('jword/newcurve.html',context_instance=RequestContext(request)) 


# 记忆曲线进度代码列表
def curvecodelist(request):
    if request.method == "GET":
        results = ProCode.objects.order_by('fstateid')
        return render_to_response('admin/procodelist.html',{'codelists':results},context_instance=RequestContext(request))
    if request.method == "POST":
        form = ProcodeForm(request.POST)
        if form.is_valid():
#            rdata =form.cleaned_data
            form.save(commit=True)
    form = ProcodeForm()


# 增加记忆曲线进度代码
def curvecode(request):
    if request.method == "POST":
        if request.POST.has_key("new"):
            form = ProcodeForm
            return render_to_response('admin/procode.html',{'proform':form},context_instance=RequestContext(request))
        if request.POST.has_key("edit"):
            editcode = ProCode.objects.get(pk=request.POST.get('wordkey',''))
            form = ProcodeForm(instance=editcode)                
            return render_to_response('admin/procode.html',{'proform':form,'objkey':editcode.pk},context_instance=RequestContext(request))            
        if request.POST.has_key("save"):   # 存储修改         
            editcode = ProCode.objects.get(pk=request.POST.get('sendkey',''))
            if editcode:
                form = ProcodeForm(request.POST,instance=editcode)
            else:                  
                form = ProcodeForm(request.POST)            
            if form.is_valid():
                form.save()                    
#            return render_to_response('user/procodelist.html',{'codelist':'desc':form.fstatename.data})
            return HttpResponseRedirect("/jxuexi/cclist/")  


def memcurgro(request): 
    if request.method == "POST":
        # 如果是开始记忆按钮
        if request.POST.has_key("startmem"):
            curgroup = CurveGroup.objects.get(pk=request.POST.get('value','')) 
            #db.get(db.Key(request.POST.get('value')))
            results = NewWord.objects.filter(fdate__gte=curgroup.fcurveword.fsdate,fdate__lte=curgroup.fcurveword.fedate)
            wordlist = results[curgroup.fcurveword.fnumlimit*(curgroup.fgroupnum-1):curgroup.fcurveword.fnumlimit*(curgroup.fgroupnum)]
            return render_to_response('jword/groupmem.html',{'curgroup':curgroup,'wordlist':wordlist},context_instance=RequestContext(request))         

        # 如果是记忆完成按钮
        if request.POST.has_key("finish"):
            #addtestval.addval('groupkey',request.POST.get('groupkey',''))
            curgroup = CurveGroup.objects.get(pk=request.POST.get('groupkey','')) 
            results = ProCode.objects.filter(fstateid=curgroup.fstateid.fstateid+1)
            for state in results:
                curgroup.fstateid = state
                curgroup.fftime = datetime.datetime.now()
                curgroup.fntime = datetime.datetime.now()+datetime.timedelta(hours=state.fnexttime)
                if state.fstateid == 8:   # 完成记忆步骤
                    curgroup.ffmemory = True
                curgroup.save()
            return HttpResponseRedirect('/jxuexi/curvemem/') 