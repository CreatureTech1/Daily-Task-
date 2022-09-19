from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#Create for views
from . forms import RegForm, DriverForm
from . models import Reg,Driver

def registerPage(request):
    # if request.user.is_authenticated:
    #      return redirect('register')
    # else:
    #     form = CreateUserForm()
    #     if request.method == 'POST':
    #         form = CreateUserForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             user = form.cleaned_data.get('username')
    #             messages.success(request,'Account was created for ' + user)
    #             return redirect('login')
    #     # context = {'form': form}
            # reg = RegForm()
    if request.method == 'POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()

        return render(request, 'registration/register.html',{'form':form})

    

def page1(request):

    reg = RegForm()
    return render(request,'page1.html',{'form':reg})

def page2(request):

    dri = DriverForm()
    return render(request,'page2.html',{'form':dri})

def profile(request):
    return render(request,'profile.html')

def LoginView(request):
    return render(request,'login.html')
# @login_required