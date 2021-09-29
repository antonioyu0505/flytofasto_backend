from django.contrib import admin
from .models import Airline, Credit_card, Customer, Flight, Location, Ticket

# Register your models here.
admin.site.register(Customer)
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Location)
admin.site.register(Ticket)
admin.site.register(Credit_card)