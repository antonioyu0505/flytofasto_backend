from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
  country = CountrySerializer()
  class Meta:
    model = Province
    fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
  province = ProvinceSerializer()
  class Meta:
    model = City
    fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = '__all__'

class AirlineSerializer(serializers.ModelSerializer):
  class Meta:
    model = Airline
    fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
  arrival_city = LocationSerializer()
  departure_city = LocationSerializer()
  airline = AirlineSerializer()
  class Meta:
    model = Flight
    fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = '__all__'

  def create(self, validated_data):
    return Customer.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.lastname = validated_data.get('lastname', instance.lastname)
    instance.email = validated_data.get('email', instance.email)
    instance.document_type = validated_data.get('document_type', instance.document_type)
    instance.document_number = validated_data.get('document_number', instance.document_number)
    instance.save()
    return instance
    
class TicketSerializerGet(serializers.ModelSerializer):
  customer = CustomerSerializer()
  flight = FlightSerializer()
  class Meta:
    model = Ticket
    fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
  customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
  flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
  class Meta:
    model = Ticket
    fields = '__all__'

  def create(self, validated_data):
    validated_data['flight'].seats -= 1
    validated_data['flight'].save()
    return Ticket.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.seat = validated_data.get('seat', instance.seat)
    instance.customer = validated_data.get('customer', instance.customer)
    instance.flight = validated_data.get('flight', instance.flight)
    instance.save()
    return instance