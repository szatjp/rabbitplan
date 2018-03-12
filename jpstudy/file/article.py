'''
Created on 2010-10-25

@author: tongjp
'''

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.forms import *

from xuexi import bforms

def addart(request):
    if request.method == "GET":
        artform = bforms.ArticleForm()
            
    if request.method == "POST":
        artform = bforms.ArticleForm(request.POST)
        # artform.cleaned_data
        artform.save(commit=True)
        
    return render_to_response('article/articleadd.html',{'article':artform})
    
        
