# coding:utf-8

'''
Created on 2010-10-9

@author: tongjp

记录测试值到记录表
'''

from datetime import datetime

from jxuexi.models import TestValue

def addval(rname,rvalue):
    testvalue=TestValue(fname=rname,
                        fvalue=rvalue,
                        ftime=datetime.now())
    testvalue.save()
    
