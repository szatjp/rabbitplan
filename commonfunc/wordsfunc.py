# -*- coding: utf-8 -*-

'''
Created on 2018年6月21日

@author: matsui
'''

from dictdata.models import JaWord,CnWord,EnWord,En2Cn,Ja2En,Ja2Cn
from django.db.models import Q

# 查询单词
def findwords(ptype,pword):
    pdict = {}
    if ptype=='cn2en': # 中英
        cnwords = CnWord.objects.filter(fword__icontains=pword)
        if cnwords:
            transword = En2Cn.objects.values_list('fcnword__fwordno', 'fcnword__fword','fcnword__fpronunciation','fenword__fwordno', 'fenword__fword').filter(fcnword__fword__icontains=pword)
            pdict['wordli'] = transword #EnWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
            pdict['lang'] = 'cn'
    elif ptype=='en2cn': # 英中
        enwords = EnWord.objects.filter(fword__icontains=pword)
        if enwords:
            transword = En2Cn.objects.values_list('fenword__fwordno', 'fenword__fword', 'fenword__fpronunciation', 'fcnword__fwordno', 'fcnword__fword').filter(fenword__fword__icontains=pword)
            pdict['wordli'] = transword #CnWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
            pdict['lang'] = 'en'
    elif ptype=='cn2jp': # 中日
        cnwords = CnWord.objects.filter(fword__icontains=pword)
        if cnwords:
            transword = Ja2Cn.objects.values_list('fcnword__fwordno', 'fcnword__fword','fcnword__fpronunciation','fjaword__fwordno', 'fjaword__fword').filter(fcnword__fword__icontains=pword)
            pdict['wordli'] = transword #JaWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
            pdict['lang'] = 'cn'
    elif ptype=='jp2cn': # 日中
        jawords = JaWord.objects.filter(Q(fword__startswith=pword)|Q(fpronunciation__startswith=pword))
        if jawords:
            #ids = Ja2Cn.objects.values_list('fcnword__fwordno', flat=True).filter(fjaword__fword__icontains=pword)
            transword = Ja2Cn.objects.values_list('fjaword__fwordno', 'fjaword__fword', 'fjaword__fpronunciation', 'fcnword__fwordno', 'fcnword__fword').filter(fjaword__fword__icontains=pword)
            #pdict['wordli'] = CnWord.objects.values('fwordno','fword','fpronunciation').filter(fwordno__in=ids).order_by('fword')
            pdict['wordli'] = transword
            pdict['lang'] = 'ja'
    return pdict
    