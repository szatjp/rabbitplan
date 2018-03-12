# coding:utf-8
'''
Created on 2010-8-27

@author: tongjp
'''
from google.appengine.ext import db
import datetime
from xuexi import models

def planengender():
    result = db.GqlQuery("select * from Plan where edate<:vdate and avail=True",vdate=datetime.date.today())
    for plan in result:
        plan.avail = False
        plan.put()

    result = db.GqlQuery("select * from Plan where sdate<=:vdate and avail=True",vdate=datetime.date.today())
#    planhis = db
    for doplan in result:
        doitem=models.Planhis(
                dodate = datetime.date.today(),
                user = doplan.user,
                planitem = doplan.key(),
                fplan = False
                )
        doitem.put()
#    return HttpResponse("任务完成！")

planengender()

       
    
