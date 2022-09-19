from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register.html',views.registerPage,name="register"),
    path('page1.html',views.page1,name="page1"),
    path('page2.html',views.page2,name="page2"),
    path('profile.html',views.profile,name="profile"),
    path('login.html', LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(next_page='page1'),name="logout"),
      
]