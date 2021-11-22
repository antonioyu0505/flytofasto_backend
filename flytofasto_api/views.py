import django
from rest_framework import generics, status
from rest_framework.response import Response

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

class TicketList(generics.ListCreateAPIView):
  queryset = Ticket.objects.all()

  def get_serializer_class(self):
    if self.request.method == 'GET':
      return TicketSerializerGet
    return TicketSerializer

  def get_queryset(self):
    queryset = Ticket.objects.all()
    document_type = self.request.query_params.get('document-type', None)
    document_number = self.request.query_params.get('document-number', None)
    if document_type is not None and document_number is not None:
      queryset = queryset.filter(customer__document_type=document_type, customer__document_number=document_number)
    return queryset

  def create(self, request, *args, **kwargs):
    try:
      customer = Customer.objects.get(document_type=request.data['customer']['document_type'], document_number=request.data['customer']['document_number'])
    except Customer.DoesNotExist:
      customer_serializer = CustomerSerializer(data=request.data['customer'])
      if customer_serializer.is_valid():
        customer = customer_serializer.save()
      else:
        return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    request.data['customer'] = customer.id
    return super().create(request, *args, **kwargs)

class TicketDetail(generics.RetrieveUpdateAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializerGet

# TODO: Add a view for the credit card information
# TODO: Add a view to retrieve the customer's tickets