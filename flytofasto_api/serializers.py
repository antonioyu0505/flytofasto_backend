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
  location_to = LocationSerializer()
  location_from = LocationSerializer()
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