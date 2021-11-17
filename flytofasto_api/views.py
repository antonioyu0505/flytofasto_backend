from rest_framework import generics

from .serializers import CitySerializer, CustomerSerializer, FlightSerializer, TicketSerializer, TicketSerializerGet
from .models import City, Customer, Flight, Ticket

class CustomerList(generics.ListCreateAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CityList(generics.ListAPIView):
  serializer_class = CitySerializer

  def get_queryset(self):
    queryset = City.objects.all()
    name = self.request.query_params.get('name', None)
    if name is not None:
      queryset = queryset.filter(name__istartswith=name)
    return queryset

class FlightList(generics.ListAPIView):
  serializer_class = FlightSerializer

  def get_queryset(self):
    queryset = Flight.objects.all()
    departure_city = self.request.query_params.get('departure-city', None)
    arrival_city = self.request.query_params.get('arrival-city', None)
    departure_date = self.request.query_params.get('departure-date', None)
    if departure_city is not None and arrival_city is not None and departure_date is not None:
      queryset = queryset.filter(departure_city=departure_city, arrival_city=arrival_city, departure__contains=departure_date)
    return queryset

# FIXME: If customer exists, ticket creation is not possible
class TicketList(generics.ListCreateAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer

class TicketDetail(generics.RetrieveUpdateAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializerGet

# TODO: Add a view for the credit card information
# TODO: Add a view to retrieve the customer's tickets