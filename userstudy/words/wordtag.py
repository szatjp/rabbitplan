'''
Created on 2018年10月22日

@author: matsui
'''




from django.http import HttpResponseRedirect
from django.shortcuts import render

from dictdata.models import CnWord,EnWord,JaWord
from userstudy.models import JpNewWord,CnNewWord,WordClass



# 选择标签页面
def selecttag(request,lang,wordno):
    curuser = request.user
    wordclassli = WordClass.objects.values('fid','fclassname').filter(fuser=curuser)
    if lang=='ja':
        selword = JaWord.objects.values('fwordno','fword').filter(pk=wordno)
    if lang=='cn':
        selword = CnWord.objects.values('fwordno','fword').filter(pk=wordno)
    if lang=='en':
        selword = EnWord.objects.values('fwordno','fword').filter(pk=wordno)
    return render(request,'wordtag/selecttag.html',{"wordclassli":wordclassli,"selword":selword})
    

# 将查询的单词添加到生词表
def findtonew(request,lang,newword):
    if request.method == "GET":
        curuser = request.user #User.objects.get(pk=request.user.pk)
        if lang=='ja':
            jword = JaWord(pk=newword)
            wordobjs = JpNewWord.objects.filter(fnewword=jword,fuser=curuser)     
            # 如用户已存在此生词，陌生度加1      
            if wordobjs:
                for wordobj in wordobjs:
                    levnum=wordobj.flevnum+1
                    wordobj.flevnum=levnum
            else:
                wordobj = JpNewWord(
                                fuser=curuser,
                                fnewword=jword,
                                flevnum=1,
                                     )
            wordobj.save()
        if lang=='cn':
            word = CnWord(pk=newword)
            wordobjs = CnNewWord.objects.filter(fnewword=word,fuser=curuser)     
            # 如用户已存在此生词，陌生度加1      
            if wordobjs:
                for wordobj in wordobjs:
                    levnum=wordobj.flevnum+1
                    wordobj.flevnum=levnum
            else:
                wordobj = CnNewWord(
                                fuser=curuser,
                                fnewword=word,
                                flevnum=1,
                                     )
            wordobj.save()
    # 返回调用的页面
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))