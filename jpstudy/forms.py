# coding:utf-8

'''
Created on 2014-4-9

@author: tong
'''

from django import forms

from commonmd.models import ProCode
from jpstudy.models import CurveWord


# 日语单词输入表单
class JwordForm(forms.Form):
    jword = forms.CharField(label="单词",required=True)
    pronunciation = forms.CharField(label="读音",required=False)
    wordclass = forms.CharField(label="词性",required=False)
    cword = forms.CharField(label="释义",required=True)
    sentence = forms.CharField(label="例句",required=False)
    paraphrase = forms.CharField(label="译文",required=False)
    
class CurveSel(forms.ModelForm):
    class Meta:
        model = CurveWord
        exclude = ('fuser','fgroupclass')
        
class ProcodeForm(forms.ModelForm):
    class Meta:
        model = ProCode
        fields = ['fstateid','fstatename','fnexttime']