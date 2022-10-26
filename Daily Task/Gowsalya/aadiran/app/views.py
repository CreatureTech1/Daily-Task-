from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from app.models import EnqInsert, Subscription
from django.db import connection
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, "app/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('index')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('index')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        
        return redirect('signin')
        
        
    return render(request, "app/signup.html")





def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "app/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('index')
    
    return render(request, "app/signin.html")
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')



@login_required(login_url='app/signin')

def booking(request):
    return render(request, "booking.html")

def layout(request):
    return render(request, "layout.html")

def bookinglist(request):
    return render(request, "bookinglist.html")

def ticketlist(request):
    return render(request, "ticketlist.html")

def seat(request):
    return render(request, "seat.html")

def bali(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "bali.html")


def shirdi(request):
    return render(request, "shirdi.html")

def home1(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "home1.html")

def enquire(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:        
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('packages.html')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('home1.html')        
    else:
        form=CreateUserForm()        
        return render(request,"enquire.html",{'form':form})

   
def goa(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "goa.html")

def kerala(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "kerala.html")

def kodaikanal(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "kodaikanal.html")
    
def manali(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "manali.html")

def thailand(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, "thailand.html")

def packages(request):
        return render(request, "packages.html")

def header(request):
        return render(request, "header.html")

def saveenq(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        city=request.POST.get('city')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        travel_destination=request.POST.get('travel_destination')
        date=request.POST.get('date')
        no_of_person=request.POST.get('no_of_person')
        vacation_type=request.POST.get('vacation_type')
        en=EnqInsert(name=name,city=city,email=email,phone_number=phone_number,travel_destination=travel_destination,date=date,no_of_person=no_of_person,vacation_type=vacation_type)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Profile has updated successfully!')
    return render(request, 'home1.html')

def privacy(request):
        return render(request, "privacy.html")

def base(request):
    if request.method=='POST':
        mail=request.POST.get('mail')
        en=Subscription(mail=mail)
        en.save()
        messages.add_message(request, messages.INFO, 'Your Subscribe has updated successfully!')
    return render(request, "home1.html")
        
def subscription(request):
    # if request.method=='POST':
        # mail=request.POST.get('mail')
        # sub=Subscription(mail=mail)
        # sub.save()
        # messages.add_message(request, messages.INFO, 'Your Subscribe has updated successfully!')
        # html_template = 'subscription.html'
        # html_message = render_to_string(html_template)
        # subject = 'Welcome to Service-Verse'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [mail]
        # message = EmailMessage(subject, html_message,email_from, recipient_list)
        # message.content_subtype = 'html'
        # message.send()
    return render(request, "home1.html")


