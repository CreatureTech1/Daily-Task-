from django.urls import path
from matrimony import views

urlpatterns = [
    path('',views.index,name="index"), 
    path('index1.html',views.index1,name="index1"),
    path('index2.html',views.index2,name="index2"), 
      
]