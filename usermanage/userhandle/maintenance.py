# coding:utf-8

'''
Created on 2013-6-21

@author: tong
'''

from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy


from usermanage.appform.userforms import UserCreateForm


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            reguser = form.clean()
            user = User.objects.create_user(username=reguser['username'],
                                            email='smc-oa@matsui.com.cn',
                                            password=reguser['password'],
                                            )
            #user.last_name=reguser['last_name']
            #user.first_name=reguser['first_name']
            if reguser['is_staff']:
                user.is_staff=True
            else:
                user.is_staff=False
            if reguser['is_superuser']:
                user.is_superuser=True
            else:
                user.is_superuser=False               
            user.save()
            return HttpResponseRedirect("/userlist/")
    else:
        form = UserCreateForm()
    return render(request,"registration/register.html", {
        'form': form,
    })
    

class Register(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    
'''    
def register(request):
    if request.method != 'POST':
        form = UserCreateForm()
    else:
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context) 
'''