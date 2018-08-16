# coding:utf-8

'''
Created on 2018年8月16日

@author: matsui
'''

from django import template


register = template.Library()


@register.filter(name='strtoli')
def strtoli(value): # 字符串转列表
    li = value.replace(",","\n")
    return li

@register.filter(name='listsum')
def listsum(value,arg): # 列表合计
    return sum(d.get(arg) for d in value)
    #return sum(d.fpuramountdis for d in value)

@register.filter(name='modelname') 
def class_name(obj): # 取得model实例的model class 名称
    return obj.__class__.__name__ 