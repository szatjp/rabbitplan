# coding:utf-8

'''
Created on 2018年6月25日

@author: matsui
'''

from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from dictdata.models import JaWord,CnWord,EnWord

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