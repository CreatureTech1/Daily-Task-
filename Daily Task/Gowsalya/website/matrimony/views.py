from django.http import HttpResponse
from django.shortcuts import render
from matrimony.forms import BioForm,SignForm
from matrimony.models import Bio,Sign

def index(request):

    bio = BioForm()
    return render(request,'index.html',{'form':bio})

def index1(request):

    return render(request, 'index1.html')

def index2(request):

    sign = SignForm()
    return render(request, 'index2.html',{'form':sign})
    
