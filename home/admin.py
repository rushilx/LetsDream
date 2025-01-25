from django.contrib import admin
from home.models import Contact
from .models import FAQ
from .forms import FAQForm
from .models import Ticket
from .models import Car
# Register your models here.
admin.site.register(Contact)


class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = ('question', 'answer')
    search_fields = ('question',)

admin.site.register(FAQ, FAQAdmin)

admin.site.register(Ticket)

# register car model for the admin 


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day', 'availability')  # Fields to display in the list view
    search_fields = ('name',)  # Add a search bar for car names
    list_filter = ('availability',)  # Filter by availability
    list_editable = ('price_per_day', 'availability')  # Make fields editable in the list view
    ordering = ('-id',)  # Sort by most recently added