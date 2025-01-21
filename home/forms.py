from django import forms
from .models import Booking
from .models import FAQ
from .models import Ticket

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['location', 'date', 'car']

        widgets = {
            'date': forms.SelectDateWidget(years=range(2025, 2031)),  # Date picker widget
        }

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message']