from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['location', 'date', 'car']

        widgets = {
            'date': forms.SelectDateWidget(years=range(2025, 2031)),  # Date picker widget
        }
