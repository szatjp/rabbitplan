# coding:utf-8

'''
Created on 2014-4-9

@author: tong
'''


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q

from dictdata.models import JaWord   #,Nword,MaxNo,CurveGroup,
from jpstudy.models import NewWord  
#from jpstudy.forms import JwordForm
from jpstudy.sysfunc.commfunc import makecode

# 打开记忆曲线法主页面
'''def curvemain(request):
    if request.method == "GET":
        curuser = request.user
#        results = models.CruveGroup.all()
#        results = results.filter('fuser=', curuser) 
        cglist = CurveGroup.objects.filter(fuser=curuser)[:100]
        return render_to_response('jword/curve.html',{'wglist':cglist,'userinfo':curuser},context_instance=RequestContext(request))
'''
    
'''
# 单词添加
def wordadd(request):
    # 如果没有登录，转向登录页
    if request.user.is_authenticated() == False:
        return render_to_response('login.html')

    # 当提交单词时，如有例句，先保存例句，再保存单词
    if request.method == 'POST':
        wordform = JwordForm(request.POST)
        if MaxNo.objects.filter(flanguage='ja').exists(): # 取得最大单词编号
            maxrec = MaxNo.objects.get(flanguage='ja')
        if wordform.is_valid():
            vword = wordform.cleaned_data

            #如果wordkey值不为空，则表示为修改
            if request.POST.get('wordkey','')!='':  # 修改的处理
                word = JaWord.objects.get(request.POST.get('wordkey',''))
                word.fjword=(request.POST.get('jword','')).strip()
                word.fpronunciation=request.POST.get('pronunciation','').strip()
                word.fcword=request.POST.get('cword','').strip()
                word.save()
                
                wordform = JwordForm()
                #返回最近添加的10单词列表    
                wordlist=JaWord.objects.order_by("-fdate")[:10]
                #wordlist=sword.fetch(10)
                return render_to_response('jword/wordadd.html', {'jwordform':wordform,'jword':wordlist},context_instance=RequestContext(request))                

         
            #检验单词是否已经存在
            vjword=vword['jword']            
            results = JaWord.objects.filter(fjword=vjword) 
            # 判断单词是否已存在
            if results.count()!=0:
                return render_to_response('jword/wordadd.html', {'jwordform':wordform},context_instance=RequestContext(request))
           
            else:
                jword = JaWord(
                            fwordno = makecode(maxrec.fmaxno,'ja',8),  
                            fjword = vword['jword'],
                            fpronunciation = vword['pronunciation'],
                            fwordclass = vword['wordclass'],
                            fcword = vword['cword'],
                            fuser = request.user.username,
                            )
                jword.save()
                maxrec.fmaxno = jword.fwordno
                maxrec.save()    
                wordform = JwordForm()
                #返回最近添加的10单词列表    
                #username = request.user.username
                wordlist=JaWord.objects.order_by("-fdate")[:20]
                return render_to_response('jword/wordadd.html', {'jwordform':wordform,'jword':wordlist},context_instance=RequestContext(request))
    else:    
        # 非post方式时，返回空表
        wordform = JwordForm()

    #返回最近添加的10单词列表    
    wordlist = JaWord.objects.order_by("-fdate")[:10]
#    for wordlist in results:
#    username = request.user.username
    return render_to_response('jword/wordadd.html', {'jwordform':wordform,'jword':wordlist,'pword':None},context_instance=RequestContext(request))

# 单词修改
def wordedit(request):
    if request.method == "POST":
#        print request.POST.kkk
        fword = request.POST.get('wordkey','')
        word = JaWord.objects.get(pk=fword)
#        wordform = bforms.JwordForm(word)
        if word.fsentence==None:
            wfsentence=""
            wfparaphrase=""
        else:
            wfsentence=word.fsentence.fsentence
            wfparaphrase=word.fsentence.fparaphrase               
        wordform = JwordForm(initial={        
        'jword':word.fjword,
        'pronunciation':word.fpronunciation,
        'cword':word.fcword,
        'sentence':wfsentence,
        'paraphrase':wfparaphrase})
     
    else:
        wordform=JwordForm()
        
    wordlist=JaWord.objects.order_by("-fdate")
    Wordkey=(request.POST.get('wordkey','')).strip()
    return render_to_response('jword/wordadd.html', {'jwordform':wordform,'jword':wordlist,'wordkey':Wordkey},context_instance=RequestContext(request))
'''

# 单词查询
def findword(request):
    if request.method == "POST":
        fword = request.POST.get('word','')
        fword = fword.strip() #去除两端空格
        #调用查询函数
        qrydict = {}
        qrydict["jword"] = JaWord.objects.filter(Q(fword__startswith=fword)|Q(fpronunciation__startswith=fword)) #findword(fword)      
        #如果没有查到单词
        if qrydict == None:
            noword='y'
            return render_to_response('person/myfind.html',{'sword':fword,'noword':noword},context_instance=RequestContext(request))             
        else:
            qrydict["sword"]=fword
            qrydict["noword"]='n'              
            return render_to_response('person/myfind.html',qrydict,context_instance=RequestContext(request))
    else:
        return render_to_response('person/myfind.html',context_instance=RequestContext(request))
    

# 将查询的单词添加到生词表
def findtonew(request,newword):
    if request.method == "GET":
        curuser = request.user #User.objects.get(pk=request.user.pk)
        jword = JaWord(pk=newword)
        wordobj = NewWord.objects.filter(fjword=jword,fuser=curuser)     
        # 如用户已存在此生词，陌生度加1
        if wordobj:
            for newword in wordobj:
                levnum=newword.flevnum+1
                newword.flevnum=levnum
        else:
            newword = NewWord(
                            fuser=curuser,
                            fjword=jword,
                            flevnum=1,
                                 )
        newword.save()
    # 返回调用的页面
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

'''
# 生词表 和 生词测试 公用
def studynword(request,drict):
    user = request.user
    # 调用查生词过程
    results = Nword.objects.filter(fuser=user)
    return render_to_response('jword/newword.html', {'newword':results},context_instance=RequestContext(request)) 
'''