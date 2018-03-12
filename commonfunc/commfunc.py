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
    newnum = int(lastno[len(prestr):dig])+1
    codenum = prestr+str(newnum).zfill(dig-len(prestr))
    return codenum

# 自定义的四舍五入函数
def myround(par,l):
    temp = 1
    for i in range(l):
        temp*=10
        v = int((par+0.5/temp)*temp) / temp
    return v

# 计划和实际的项目检验， 计划有的项目实际必须有，计划为空的实际必须也为空
def plancheck(planobj,factobj,fieldli):   # planobj 计划对象,factobj 实际对象,fieldli 要检查的字段
    redict = {}
    redict["mis"] = 1
    redict["maxdate"] = None
    for getfield in fieldli:
        if planobj.__getattribute__(getfield):
            if not factobj.__getattribute__(getfield):
                redict["mis"] = 0
                #return '0'
            else:
                if redict["maxdate"]:
                    if factobj.__getattribute__(getfield)>redict["maxdate"]:
                        redict["maxdate"] = factobj.__getattribute__(getfield)
                else:
                    redict["maxdate"] = factobj.__getattribute__(getfield)
        else:
            if factobj.__getattribute__(getfield):
                redict["mis"] = 0
                #return '0'
    return redict