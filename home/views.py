from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .forms import BookingForm
# Create your views here.
def base(request):
    current_year = datetime.now().year
    return render(request, 'base.html', {'current_year': current_year})

@auth
def index(request):
    messages.success(request, "How Are You Doing Friends")
    return render(request, 'index.html')

def index2(request):
    messages.success(request, "How Are You Doing Friends")
    return render(request, 'index2.html')

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
@guest
def register_view(request):
   if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('index')
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
            form.save()  # Save the booking data to the database
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')
