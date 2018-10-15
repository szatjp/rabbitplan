# coding:utf-8

'''
Created on 2018年6月25日

@author: matsui
'''
from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from django.db.models import Max

from commonfunc.commfunc import makecode

from dictdata.models import JaWord,CnWord,EnWord


def funaddword(wtype,pusername,worddict):
    prestr = wtype
    statu = 'Success'
    wordobj = None
    errinfo = ''
    # 增加日语单词
    if wtype == 'ja':
        lastno = JaWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']
        wordno = makecode(maxno,prestr,8)
        wordobj = JaWord()
        wordobj.fwordno = wordno
        wordobj.fword = worddict['word']
        wordobj.fpronunciation = worddict['pronunciation']
        #wordobj.fwordclass =
        wordobj.fuser = pusername        
        try:
            wordobj.save()
        except:
            statu = 'Fail'
            errinfo = "新增失败，请检查！"
            #return render(request,'inbill/billerror.html',{"errinfo":errinfo})
    # 增加中文单词
    if wtype == 'cn':
        lastno = CnWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']
        wordno = makecode(maxno,prestr,8)
        wordobj = CnWord()
        wordobj.fwordno = wordno
        wordobj.fword = worddict['word']
        wordobj.fpronunciation = worddict['pronunciation']    
        try:
            wordobj.save()
        except:
            statu = 'Fail'
            errinfo = "新增失败，请检查！"
            #return render(request,'inbill/billerror.html',{"errinfo":errinfo})
    if wtype == 'en':
        lastno = EnWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']
        wordno = makecode(maxno,prestr,8)
        wordobj = EnWord()
        wordobj.fwordno = wordno
        wordobj.fword = worddict['word']
        wordobj.fpronunciation = worddict['pronunciation']      
        try:
            wordobj.save()
        except:
            statu = 'Fail'
            errinfo = "新增失败，请检查！"
            #return render(request,'inbill/billerror.html',{"errinfo":errinfo})        
    return {"statu":statu,"wordobj":wordobj,"info":errinfo}