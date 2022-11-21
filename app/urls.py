from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('app/signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('booking.html', views.booking, name='booking'),
    path('bookinglist.html', views.bookinglist, name='bookinglist'),
    path('ticketlist.html', views.ticketlist, name='ticketlist'),
    path('seat.html', views.seat, name='seat'),
    path('bali.html', views.bali, name='bali'),
    path('shirdi.html', views.shirdi, name='shirdi'),
    path('home1.html', views.home1, name='home1'),
    path('enquire.html', views.enquire, name='enquire'),
    path('goa.html', views.goa, name='goa'),
    path('kerala.html', views.kerala, name='kerala'),
    path('kodaikanal.html', views.kodaikanal, name='kodaikanal'),
    path('manali.html', views.manali, name='manali'),
    path('thailand.html', views.thailand, name='thailand'),
    path('packages.html', views.packages, name='packages'),
    path('header.html', views.header, name='header'),
    path('saveenq',views.saveenq,name='saveenq'),
    path('privacy.html',views.privacy,name='privacy'),
    path('base.html',views.base,name='base'),
    path('subscription',views.subscription,name='subscription'),
   
]






