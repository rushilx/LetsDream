from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def base(request):
    current_year = datetime.now().year
    return render(request, 'base.html', {'current_year': current_year})


def index(request):
    context = {
        
        # "variable1": "this is great",
        # "variable2": "this is great"
    }
    messages.success(request, "How Are You Doin Friends")
    return render(request, 'index.html', context)

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
