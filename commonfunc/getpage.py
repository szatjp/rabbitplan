# coding:utf-8

'''
Created on 2011-11-7

@author: tongjp
'''

'''
# 返回生词列表
def pagenword(request,puser):
    results=db.GqlQuery("SELECT * FROM Nword where fuser=:vuser",vuser=puser)
    paginator=Paginator(results,10)
    # 确信Request要求是个整数，负责返回1
    if request.method == "GET":
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1 
        # 如果页码要就超出范围，返回最后一页
        try:
            wordlist = paginator.page(page)
        except (EmptyPage, InvalidPage):
            wordlist = paginator.page(paginator.num_pages)
        return wordlist
    
    if request.method == "POST":
#        assert False
        try:
            # 返回要求的网址
            httpstr = str(request.META.get('HTTP_REFERER'))
            # 找出页数
            page=int(httpstr[httpstr.index('=',0)+1:])
        except ValueError:
            page = 1 
            
        # 如果页码要就超出范围，返回最后一页
        try:
            wordlist = paginator.page(page)
        except (EmptyPage, InvalidPage):
            wordlist = paginator.page(paginator.num_pages)
        return wordlist 
        
    '''