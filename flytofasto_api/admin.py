from django.contrib import admin
from .models import Airline, CreditCard, Customer, Flight, Country, Ticket, Province, City

# Register your models here.
admin.site.register(Customer)
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Country)
admin.site.register(Ticket)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(CreditCard)