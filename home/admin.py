from django.contrib import admin
from home.models import Contact
from .models import FAQ
from .forms import FAQForm
from .models import Ticket

# Register your models here.
admin.site.register(Contact)


class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = ('question', 'answer')
    search_fields = ('question',)

admin.site.register(FAQ, FAQAdmin)

admin.site.register(Ticket)