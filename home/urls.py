from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path("", views.index, name='home'),
    path("signup", views.signup, name='signup'),
    path('login', views.loginUser, name="login"),
    path("service", views.service, name='service'),
    path('logout', views.logoutUser, name="logout"),
    path("contact", views.contact, name='contact')
]
# sachin*123 thisis123@
