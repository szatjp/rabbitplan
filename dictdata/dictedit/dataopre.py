# coding:utf-8

'''
Created on 2016-1-18
字典操作模块
@author: tjp
'''

from django.db.models import Max

from rest_framework import generics

from commonfunc.commfunc import makecode
from dictdata.models import JaWord, CnWord, EnWord
from dictdata.dictedit.dataserialize import JawordSeria, CnwordSeria, EnwordSeria


class JpList(generics.ListCreateAPIView):
    queryset = JaWord.objects.all()
    serializer_class = JawordSeria
    def perform_create(self, serializer):
        prestr = 'ja'
        lastno = JaWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']        
        serializer.save(fwordno=makecode(maxno,prestr,8),fuser='sunny_tong')


class JpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JaWord.objects.all()
    serializer_class = JawordSeria
    

class CnList(generics.ListCreateAPIView):
    queryset = CnWord.objects.all()
    serializer_class = CnwordSeria
    def perform_create(self, serializer):
        prestr = 'cn'
        lastno = CnWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']        
        serializer.save(fwordno=makecode(maxno,prestr,8),fuser='sunny_tong')


class CnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CnWord.objects.all()
    serializer_class = CnwordSeria
    

class EnList(generics.ListCreateAPIView):
    queryset = EnWord.objects.all()
    serializer_class = EnwordSeria
    def perform_create(self, serializer):
        prestr = 'en'
        lastno = EnWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']        
        serializer.save(fwordno=makecode(maxno,prestr,8),fuser='sunny_tong')


class EnDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnWord.objects.all()
    serializer_class = EnwordSeria