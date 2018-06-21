# -*- coding: utf-8 -*-

'''
Created on 2018年6月21日

@author: matsui
'''

from dictdata.models import JaWord,CnWord,EnWord,En2Cn,Ja2En,Ja2Cn
from django.db.models import Q

# 查询单词
def findword(pdict,pword):
    if pdict=='cn2en':
        cnwords = CnWord.objects.filter(fword__icontains=pword)
        if cnwords:
            wordli = En2Cn.objects.filter(fcnword__fword__icontains=pword).order_by('fcnword')
    elif pdict=='en2cn':
        enwords = EnWord.objects.filter(fword__icontains=pword)
        if enwords:
            wordli = En2Cn.objects.filter(fenword__fword__icontains=pword).order_by('fenword')
    elif pdict=='cn2jp':
        cnwords = CnWord.objects.filter(fword__icontains=pword)
        if cnwords:
            wordli = Ja2Cn.objects.filter(fcnword__fword__icontains=pword).order_by('fcnword')
    elif pdict=='jp2cn':
        jawords = JaWord.objects.filter(Q(fword__startswith=pword)|Q(fpronunciation__startswith=pword))
        if jawords:
            wordli = Ja2Cn.objects.filter(fjaword__fword__icontains=pword).order_by('fjaword')
    