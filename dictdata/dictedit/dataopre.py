# coding:utf-8

'''
Created on 2016-1-18
字典操作模块
@author: tjp
'''

from django.db.models import Max

from rest_framework import generics
from django_filters import rest_framework as filters

from commonfunc.commfunc import makecode
from dictdata.models import JaWord, CnWord, EnWord
from dictdata.dictedit.dataserialize import JawordSeria, CnwordSeria, EnwordSeria


class JpFilter(filters.FilterSet):
    freshdate = filters.IsoDateTimeFilter(name="fdate", lookup_expr='gte')
    class Meta:
        model = JaWord
        fields = ['fwordno','fword','fpronunciation','freshdate']
        
        
class JpList(generics.ListCreateAPIView):
    queryset = JaWord.objects.all()
    serializer_class = JawordSeria
    filter_class = JpFilter
    def perform_create(self, serializer):
        prestr = 'ja'
        lastno = JaWord.objects.filter().aggregate(Max('fwordno'))
        if not lastno['fwordno__max']:
            maxno = prestr+'000000'
        else:
            maxno = lastno['fwordno__max']        
        serializer.save(fwordno=makecode(maxno,prestr,8),fuser=self.request.user.first_name)


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