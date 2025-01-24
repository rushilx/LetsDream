from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("index", views.index, name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path("", views.index2, name= 'index2'),
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
    path("self_drive.html", views.self_drive_cars, name= 'self_drive'),
    path("luxury_cars.html", views.luxury_cars, name= 'luxury_cars'),
    path("admin.html", views.admin_page, name= 'admin_page'),
    path('accounts/', include('allauth.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)