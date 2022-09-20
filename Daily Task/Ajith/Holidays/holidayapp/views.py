from django.shortcuts import render

# Create your views here.
def holiday(request):
    return render(request,"holiday.html")

def home(request):
    return render(request,"home.html")
