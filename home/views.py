from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .forms import BookingForm
from django.core.mail import send_mail
from .models import FAQ
from .forms import TicketForm
from .models import Ticket 

from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    current_year = datetime.now().year
    return render(request, 'base.html', {'current_year': current_year})

# profile section

@login_required
def profile(request):
    user = request.user  # Fetch the currently logged-in user
    return render(request, 'profile.html', {'user': user})

def index2(request):
    return render(request, 'index2.html')
@auth
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        contact= Contact(name=name, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, "your message has been sent !")
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

    #  login page models date 31/12/2024 initiated
# @guest
def register_view(request):
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('index2')
        else:
            # If the form is invalid, render the form again with error messages
            return render(request, 'register.html', {'form': form})
   else:
        initial_data ={'username':'', 'password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
        return render (request, 'register.html',{'form':form}) 

@guest
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return render(request,'index.html')
        else:
            # If the form is invalid, render the form again with error messages
            return render(request, 'login.html', {'form': form})
    else:
        initial_data ={'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
        return render(request, 'login.html',{'form':form})   

def logout_view(request):
   logout(request)
   return redirect('login')


def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Now the form is valid, access the cleaned data
            location = form.cleaned_data['location']
            date = form.cleaned_data['date']
            car = form.cleaned_data['car']

            # email content
            subject = 'New Car Booking Request'
            message = f"New Booking Details:\n\nLocation: {location}\nDate: {date}\nCar: {car}"
            from_email = 'dannydroves@gmail.com'  # You can use the same as EMAIL_HOST_USER
            recipient_list = ['dannydroves@gmail.com']  # Y
            form.save() 

            send_mail(subject, message, from_email, recipient_list)
             # Save the booking data to the database
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

def submit_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associate the ticket with the logged-in user
            ticket.save()
            return redirect('ticket_submitted')
    else:
        form = TicketForm()
    return render(request, 'submit_ticket.html', {'form': form})

def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'support/ticket_list.html', {'tickets': tickets})

def self_drive_cars(request):
    return render(request, 'self_drive.html')

def luxury_cars(request):
    return render(request, 'luxury_cars.html')

# admin page
def admin_page(request):
    return render(request, 'admin.html')
