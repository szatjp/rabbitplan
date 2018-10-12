# coding:utf-8

'''
Created on 2018年6月25日

@author: matsui
'''

from django.views.generic import ListView
from django.shortcuts import render,get_object_or_404


from dictdata.models import JaWord,CnWord,EnWord,Ja2Cn


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

def transadd(request,wordno,trantype):   
    if trantype=='jatocn':
        if JaWord.objects.filter(fwordno=wordno).exists():
            wordobj = JaWord.objects.get(fwordno=wordno)
        #if Ja2Cn.objects.filter(fjaword__fwordno=wordno).exists():
        #    jatocns = Ja2Cn.objects.get(fjaword__fwordno=wordno)
    return render(request,'dictedit/transedit.html', {"word":wordobj})  