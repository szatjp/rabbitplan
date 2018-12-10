'''
Created on 2018年10月22日

@author: matsui
'''




from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from dictdata.models import JaWord,CnWord,EnWord   #,Nword,MaxNo,CurveGroup,

from commonfunc.wordsfunc import findwords

from userstudy.models import JpNewWord,CnNewWord

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
def searchword(request):
    if request.method == "POST":
        fword = request.POST.get('word','')
        voption = request.POST.getlist('options','')[0]
        fword = fword.strip() #去除两端空格
        qrydict = {}
        #调用查询函数
        result = findwords(voption,fword)
        qrydict["op"] = voption
        qrydict["wordli"] = result['wordli']      
        #如果没有查到单词
        if result['wordli'] == None:
            noword='y'
            #qrydict["wordli"] = None
            return render(request,'wordstudy/findword.html',{'sword':fword,'noword':noword},context_instance=RequestContext(request))             
        else:
            qrydict["sword"]=fword
            qrydict["noword"]='n' 
            qrydict["lang"] = result['lang']             
            return render(request,'wordstudy/findword.html',qrydict)
    else:
        return render(request,'wordstudy/findword.html')
    

# 将查询的单词添加到生词表
@login_required
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


class NewWordLi(ListView):
    paginate_by = 10
    template_name = 'newwords/newwords.html'
    def get_queryset(self):
        #self.publisher = get_object_or_404(CnWord, name=self.kwargs['fword'])
        #words = En2Cn.objects.filter(fcnword__fword__icontains=self.kwargs['fword'])
        words = JpNewWord.objects.values('fnewword__fwordno','fnewword__fword','fnewword__fpronunciation','fnewword__fwordclass').all().order_by('fnewword__fwordno')
        return words
    def get_context_data(self, **kwargs):
        """
                                      在视图函数中将模板变量传递给模板是通过给 render 函数的 context 参数传递一个字典实现的，
                                    例如 render(request, 'blog/index.html', context={'post_list': post_list})，
                                    这里传递了一个 {'post_list': post_list} 字典给模板。
                                    在类视图中，这个需要传递的模板变量字典是通过 get_context_data 获得的，
                                    所以我们复写该方法，以便我们能够自己再插入一些我们自定义的模板变量进去。
        """
        # 首先获得父类生成的传递给模板的字典。
        context = super().get_context_data(**kwargs)

        # 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
        # paginator 是 Paginator 的一个实例，
        # page_obj 是 Page 的一个实例，
        # is_paginated 是一个布尔变量，用于指示是否已分页。
        # 例如如果规定每页 10 个数据，而本身只有 5 个数据，其实就用不着分页，此时 is_paginated=False。
        # 关于什么是 Paginator，Page 类在 Django Pagination 简单分页：http://zmrenwu.com/post/34/ 中已有详细说明。
        # 由于 context 是一个字典，所以调用 get 方法从中取出某个键对应的值。
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        # 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据，见下方。
        pagination_data = self.pagination_data(paginator, page, is_paginated)

        # 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
        context.update(pagination_data)

        # 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
        # 注意此时 context 字典中已有了显示分页导航条所需的数据。
        return context
    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            # 如果没有分页，则无需显示分页导航条，不用任何分页导航条的数据，因此返回一个空的字典
            return {}

        # 当前页左边连续的页码号，初始值为空
        left = []

        # 当前页右边连续的页码号，初始值为空
        right = []

        # 标示第 1 页页码后是否需要显示省略号
        left_has_more = False

        # 标示最后一页页码前是否需要显示省略号
        right_has_more = False

        # 标示是否需要显示第 1 页的页码号。
        # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
        # 其它情况下第一页的页码是始终需要显示的。
        # 初始值为 False
        first = False

        # 标示是否需要显示最后一页的页码号。
        # 需要此指示变量的理由和上面相同。
        last = False

        # 获得用户当前请求的页码号
        page_number = page.number

        # 获得分页后的总页数
        total_pages = paginator.num_pages

        # 获得整个分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
        page_range = paginator.page_range

        if page_number == 1:
            # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
            # 此时只要获取当前页右边的连续页码号，
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
            # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            right = page_range[page_number:page_number + 2]

            # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
            # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
            if right[-1] < total_pages - 1:
                right_has_more = True

            # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
            # 所以需要显示最后一页的页码号，通过 last 来指示
            if right[-1] < total_pages:
                last = True

        elif page_number == total_pages:
            # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
            # 此时只要获取当前页左边的连续页码号。
            # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
            # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

            # 如果最左边的页码号比第 2 页页码号还大，
            # 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示。
            if left[0] > 2:
                left_has_more = True

            # 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码，
            # 所以需要显示第一页的页码号，通过 first 来指示
            if left[0] > 1:
                first = True
        else:
            # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
            # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]

            # 是否需要显示最后一页和最后一页前的省略号
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True

            # 是否需要显示第 1 页和第 1 页后的省略号
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True

        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
        }

        return data    


'''
# 生词表 和 生词测试 公用
def studynword(request,drict):
    user = request.user
    # 调用查生词过程
    results = Nword.objects.filter(fuser=user)
    return render_to_response('jword/newword.html', {'newword':results},context_instance=RequestContext(request)) 
'''