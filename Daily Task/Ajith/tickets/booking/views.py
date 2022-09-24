from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def page1(request):
    return render(request,'page1.html')