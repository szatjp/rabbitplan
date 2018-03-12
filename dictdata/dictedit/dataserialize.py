# coding:utf-8

'''
Created on 2016-1-15

@author: tjp
'''

from django.db.models import Max

from rest_framework import serializers

from commonfunc.commfunc import makecode
from dictdata.models import JaWord, CnWord, EnWord


'''
   fwordno = models.CharField(primary_key=True, max_length=8)
    fword = models.CharField(max_length=30, blank=True)
    fpronunciation = models.CharField(null=True, max_length=30, blank=True)
    fwordclass = models.CharField(null=True, max_length=30, blank=True)
    fuser = models.CharField(null=True, max_length=30, blank=True)
    fdate = models.DateTimeField(auto_now=True)
    favail = models.FloatField(null=True)
'''


class JawordSeria(serializers.ModelSerializer):
    class Meta:
        model = JaWord
        fields = ('fwordno', 'fword', 'fpronunciation',
                  'fwordclass', 'fuser', 'fdate')
        read_only_fields = ('fwordno','fuser')
        
class CnwordSeria(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CnWord
        fields = ('fwordno', 'fword', 'fpronunciation',
                  'fwordclass', 'fuser', 'fdate')
        read_only_fields = ('fwordno','fuser')

class EnwordSeria(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnWord
        fields = ('fwordno', 'fword', 'fpronunciation',
                  'fwordclass', 'fuser', 'fdate')
        read_only_fields = ('fwordno','fuser')