# -*- coding: utf-8 -*-

'''
Created on 2018年6月21日

@author: matsui
'''

from dictdata.models import JaWord,CnWord,EnWord,En2Cn,Ja2En,Ja2Cn
from django.db.models import Q

# 查询单词
def findwords(pdict,pword):
    if pdict=='cn2en':
        cnwords = CnWord.objects.filter(fword__icontains=pword)
        if cnwords:
            ids = En2Cn.objects.values_list('fenword__fwordno', flat=True).filter(fcnword__fword__icontains=pword)
            wordli = EnWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
    elif pdict=='en2cn':
        enwords = EnWord.objects.filter(fword__icontains=pword)
        if enwords:
            ids = En2Cn.objects.values_list('fcnword__fwordno', flat=True).filter(fenword__fword__icontains=pword)
            wordli = CnWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
    elif pdict=='cn2jp':
        cnwords = CnWord.objects.filter(fword__icontains=pword)
        if cnwords:
            ids = Ja2Cn.objects.values_list('fjaword__fwordno', flat=True).filter(fcnword__fword__icontains=pword)
            wordli = JaWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
    elif pdict=='jp2cn':
        jawords = JaWord.objects.filter(Q(fword__startswith=pword)|Q(fpronunciation__startswith=pword))
        if jawords:
            ids = Ja2Cn.objects.values_list('fcnword__fwordno', flat=True).filter(fjaword__fword__icontains=pword)
            wordli = CnWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
    return wordli
    