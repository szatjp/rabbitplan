# coding:utf-8

'''
Created on 2018年6月25日

@author: matsui
'''

from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from dictdata.models import JaWord,CnWord,EnWord,Ja2Cn,En2Cn,Ja2En
from dictdata.appcomm.dictedit import funaddword,addtran
from markdown.extensions import fenced_code


class WordList(ListView):
    template_name = 'books/books_by_publisher.html'
    def get_queryset(self):
        self.publisher = get_object_or_404(JaWord, name=self.kwargs['publisher'])
        return JaWord.objects.filter(publisher=self.publisher)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context 

@login_required
def transadd(request,wordno,trantype):   
    if trantype=='jatocn':
        if JaWord.objects.filter(fwordno=wordno).exists():
            wordobj = JaWord.objects.get(fwordno=wordno)
    if trantype=='cntoja':
        if CnWord.objects.filter(fwordno=wordno).exists():
            wordobj = CnWord.objects.get(fwordno=wordno)
    if trantype in ('entocn','entoja'):
        if EnWord.objects.filter(fwordno=wordno).exists():
            wordobj = EnWord.objects.get(fwordno=wordno)
    if trantype=='cntoen':
        if CnWord.objects.filter(fwordno=wordno).exists():
            wordobj = CnWord.objects.get(fwordno=wordno)            
    if request.method == "GET":
        return render(request,'dictedit/transedit.html', {"word":wordobj,"trantype":trantype}) 
    if request.method == "POST":
        #worddict = {}
        word = request.POST.get('fword','')
        pronunciation = request.POST.get('fpronunciation','')
        if trantype=='jatocn': # 日译中
            if JaWord.objects.filter(fwordno=wordno).exists():
                wordobj = JaWord.objects.get(fwordno=wordno)
                transword = CnWord.objects.filter(fword=word) # 释义的单词是否存在
                if len(transword)==0:
                    # 如果释义的单词不存在，添加该单词
                    addresult = funaddword('cn',request.user.first_name,{"word":word,"pronunciation":pronunciation})
                    if addresult['statu']=='Success':
                        transobj = addresult['wordobj']
                        ja2cnobj = Ja2Cn(
                            fjaword = wordobj,
                            fcnword = transobj,
                            fuser = request.user.first_name
                            ) 
                        ja2cnobj.save()  # 添加翻译表记录
                else:
                    # 如果单词释义存在，但单词翻译不存在，则进入翻译选择页面则添加释义表
                    #CnWord.objects.filter(fword=word).exclude(fjaword=wordobj,)
                    if len(transword)==1:
                        transobj = CnWord.objects.get(fword=word)
                        if not Ja2Cn.objects.filter(fjaword=wordobj,fcnword=transobj).exists():
                            ja2cnobj = Ja2Cn(
                                fjaword = wordobj,
                                fcnword = transobj,
                                fuser = request.user.first_name
                                )                         
                            ja2cnobj.save()
            return HttpResponseRedirect('/dict/jaword/'+wordobj.fwordno+'/update/')
        if trantype=='cntoja': # 中译日
            if CnWord.objects.filter(fwordno=wordno).exists():
                wordobj = CnWord.objects.get(fwordno=wordno)
                transword = JaWord.objects.filter(fword=word) # 释义的单词是否存在
                if len(transword)==0:
                    # 如果释义的单词不存在，添加该单词
                    addresult = funaddword('ja',request.user.first_name,{"word":word,"pronunciation":pronunciation})
                    if addresult['statu']=='Success':
                        transobj = addresult['wordobj']
                        ja2cnobj = Ja2Cn(
                            fjaword = transobj,
                            fcnword = wordobj,
                            fuser = request.user.first_name
                            ) 
                        ja2cnobj.save()  # 添加翻译表记录
                else:
                    # 如果单词释义存在，但单词翻译不存在，则进入翻译选择页面则添加释义表
                    #CnWord.objects.filter(fword=word).exclude(fjaword=wordobj,)
                    if len(transword)==1:
                        transobj = JaWord.objects.get(fword=word)
                        if not Ja2Cn.objects.filter(fjaword=wordobj,fcnword=transobj).exists():
                            ja2cnobj = Ja2Cn(
                                fjaword = transobj,
                                fcnword = wordobj,
                                fuser = request.user.first_name
                                )                         
                            ja2cnobj.save()
            return HttpResponseRedirect('/dict/cnword/'+wordobj.fwordno+'/update/')
        if trantype=='cntoen': # 中译英
            if CnWord.objects.filter(fwordno=wordno).exists():
                wordobj = CnWord.objects.get(fwordno=wordno)
                transword = EnWord.objects.filter(fword=word) # 释义的单词是否存在
                if len(transword)==0:
                    # 如果释义的单词不存在，添加该单词
                    addresult = funaddword('en',request.user.first_name,{"word":word,"pronunciation":pronunciation})
                    if addresult['statu']=='Success':
                        transobj = addresult['wordobj']
                        lang2lang = En2Cn(
                            fenword = transobj,
                            fcnword = wordobj,
                            fuser = request.user.first_name
                            ) 
                        lang2lang.save()  # 添加翻译表记录
                else:
                    # 如果单词释义存在，但单词翻译不存在，则进入翻译选择页面则添加释义表
                    #CnWord.objects.filter(fword=word).exclude(fjaword=wordobj,)
                    if len(transword)==1:
                        transobj = EnWord.objects.get(fword=word)
                        if not En2Cn.objects.filter(fcnword=wordobj,fenword=transobj).exists():
                            lang2lang = En2Cn(
                                fenword = transobj,
                                fcnword = wordobj,
                                fuser = request.user.first_name
                                )                         
                            lang2lang.save()
            return HttpResponseRedirect('/dict/cnword/'+wordobj.fwordno+'/update/')
        if trantype=='entocn':  # 英译中
            if EnWord.objects.filter(fwordno=wordno).exists():
                wordobj = EnWord.objects.get(fwordno=wordno)
                transword = CnWord.objects.filter(fword=word) # 释义的单词是否存在
                if len(transword)==0:
                    # 如果释义的单词不存在，添加该单词
                    addresult = funaddword('cn',request.user.first_name,{"word":word,"pronunciation":pronunciation})
                    if addresult['statu']=='Success':
                        transobj = addresult['wordobj']
                        lang2lang = En2Cn(
                            fenword = wordobj,
                            fcnword = transobj,
                            fuser = request.user.first_name
                            ) 
                        lang2lang.save()  # 添加翻译表记录
                else:
                    # 如果单词释义存在，但单词翻译不存在，则进入翻译选择页面则添加释义表
                    #CnWord.objects.filter(fword=word).exclude(fjaword=wordobj,)
                    if len(transword)==1:
                        transobj = CnWord.objects.get(fword=word)
                        if not En2Cn.objects.filter(fenword=wordobj,fcnword=transobj).exists():
                            lang2lang = En2Cn(
                                fenword = wordobj,
                                fcnword = transobj,
                                fuser = request.user.first_name
                                )                         
                            lang2lang.save()
            return HttpResponseRedirect('/dict/enword/'+wordobj.fwordno+'/update/')                
        if trantype=='entoja':  # 英译日
            if EnWord.objects.filter(fwordno=wordno).exists():
                wordobj = EnWord.objects.get(fwordno=wordno)
                transword = JaWord.objects.filter(fword=word) # 释义的单词是否存在
                if len(transword)==0:
                    # 如果释义的单词不存在，添加该单词
                    addresult = funaddword('ja',request.user.first_name,{"word":word,"pronunciation":pronunciation})
                    if addresult['statu']=='Success':
                        transobj = addresult['wordobj']
                        lang2lang = Ja2En(
                            fenword = wordobj,
                            fjaword = transobj,
                            fuser = request.user.first_name
                            ) 
                        lang2lang.save()  # 添加翻译表记录
                else:
                    # 如果单词释义存在，但单词翻译不存在，则进入翻译选择页面则添加释义表
                    #CnWord.objects.filter(fword=word).exclude(fjaword=wordobj,)
                    if len(transword)==1:
                        transobj = JaWord.objects.get(fword=word)
                        if not Ja2En.objects.filter(fenword=wordobj,fjaword=transobj).exists():
                            lang2lang = Ja2En(
                                fenword = wordobj,
                                fjaword = transobj,
                                fuser = request.user.first_name
                                )                         
                            lang2lang.save()
            return HttpResponseRedirect('/dict/enword/'+wordobj.fwordno+'/update/')                                    