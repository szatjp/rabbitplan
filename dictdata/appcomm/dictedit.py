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


# 添加日语单词
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


# 添加单词释义
def addtran(wordobj,transobj,trantab,requser,wdict):
    wordobj = wordobj.objects.get(fwordno=wdict['wordno']) # 取的要翻译的单词
    transword = transobj.objects.filter(fword=wdict['word']) # 释义的单词是否存在
    if len(transword)==0:
        # 如果释义的单词不存在，添加该单词
        addresult = funaddword('ja',requser,wdict)
        if addresult['statu']=='Success':
            transobj = addresult['wordobj']
            trancros = trantab(
                fjaword = wordobj,
                fcnword = transobj,
                fuser = requser
                ) 
            trancros.save()  # 添加翻译表记录
    else:
        # 如果单词释义存在，但单词翻译不存在，则进入翻译选择页面则添加释义表
        #CnWord.objects.filter(fword=word).exclude(fjaword=wordobj,)
        if len(transword)==1:  # 如果释义单词母表唯一（可能有多音字）
            transobj = transobj.objects.get(fword=wdict['word'])
            if not trantab.objects.filter(fjaword=wordobj,fcnword=transobj).exists():
                trancros = trantab(
                    fjaword = wordobj,
                    fcnword = transobj,
                    fuser = requser
                    )                         
                trancros.save()    