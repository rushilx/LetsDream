from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("index", views.index, name= 'index'),
    path("index2", views.index2, name= 'index2'),
    path("about", views.about, name= 'about'),
    path("services", views.services, name= 'services'),
    path("contact", views.contact, name= 'contact'),
    path('register/', views.register_view, name= 'register'),
    path('login/', views.login_view, name= 'login'),
    path('logout/', views.logout_view, name= 'logout'),
    path('booking/', views.booking_view, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'), 
    path('faq/', views.faq_view, name='faq'),
    path('submit-ticket/', views.submit_ticket, name='submit_ticket'),
    path('my-tickets/', views.ticket_list, name='ticket_list'),
    path('accounts/', include('allauth.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)