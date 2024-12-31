from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("index", views.index, name= 'home'),
    path("about", views.about, name= 'about'),
    path("services", views.services, name= 'services'),
    path("contact", views.contact, name= 'contact'),
    path('register/', views.register_view, name= 'register'),
    path('login/', views.login_view, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
]