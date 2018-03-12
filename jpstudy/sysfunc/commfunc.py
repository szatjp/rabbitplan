# coding:utf-8

'''
Created on 2013-11-27

@author: tong
'''

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    
# 制作一个顺序编码, lastno 上一位, prestr 前缀, dig 编码位数
def makecode(lastno,prestr,dig):
    if lastno:
        maxno=lastno
    else:
        maxno='0'
    codenum = prestr+str(int(maxno.lstrip(prestr))+1).zfill(dig-len(prestr))
    return codenum

