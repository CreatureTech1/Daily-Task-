from aup.models import inputform
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method =="POST":
        if request.POST.get('title') and request.POST.get('body'):
            input = inputform()
            input.title=request.POST.get('title')
            input.body=request.POST.get('body')
            input.save()
    return render(request,'index.html')

            


