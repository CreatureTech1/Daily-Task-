from django.shortcuts import render
from app.forms import ContactForm 

def index(request):
    con = ContactForm()
    return render(request,'index.html',{'form':con})
