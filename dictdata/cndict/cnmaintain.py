# coding:utf-8

'''
Created on 2018年7月3日

@author: matsui
'''

from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from dictdata.models import CnWord,En2Cn

class CnLilst(ListView):
    #queryset = CnWord.objects.all()
    paginate_by = 10
    template_name = 'dictedit/wordli.html'
    def get_queryset(self):
        #self.publisher = get_object_or_404(CnWord, name=self.kwargs['fword'])
        words = En2Cn.objects.filter(fcnword__fword__icontains=self.kwargs['fword'])
        return words
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context
