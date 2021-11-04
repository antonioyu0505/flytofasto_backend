from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=255)
  class Meta:
    db_table = 'country'

class Province(models.Model):
  name = models.CharField(max_length=255)
  country = models.ForeignKey(
    Country, 
    on_delete = models.CASCADE,
    db_column = 'country_id'
  )
  class Meta:
    db_table = 'province'

class City(models.Model):
  name = models.CharField(max_length=255)
  province = models.ForeignKey(
    Province, 
    on_delete = models.CASCADE,
    db_column = 'province_id'
  )
  class Meta:
    db_table = 'city'

class Airline(models.Model):
  name = models.CharField(max_length=255)

  class Meta:
    db_table = 'airline'

class Customer(models.Model):

  name = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  document_type = models.CharField(max_length=4)
  document_number = models.CharField(max_length=255)

  class Meta:
    unique_together = (('document_type', 'document_number'))
    db_table = 'customer'


class Flight(models.Model):

  departure = models.DateTimeField()
  arrival = models.DateTimeField()
  seats = models.PositiveIntegerField()
  price = models.FloatField()
  arrival_city = models.ForeignKey(
    City, 
    on_delete = models.CASCADE,
    related_name = 'arrival_city_id',
    db_column = 'arrival_city_id'
  )
  departure_city = models.ForeignKey(
    City, 
    on_delete = models.CASCADE,
    related_name = 'departure_city_id',
    db_column = 'departure_city_id'
  )
  airline = models.ForeignKey(
    Airline, 
    on_delete = models.CASCADE,
    db_column = 'airline_id'
  )

  class Meta:
    db_table = 'flight'

class Ticket(models.Model):
  seat = models.CharField(max_length=255)
  customer = models.ForeignKey(
    Customer,
    on_delete = models.CASCADE,
    db_column = 'customer_id',
    null=True
  )
  flight = models.ForeignKey(
    Flight,
    on_delete = models.CASCADE,
    db_column = 'flight_id'
  )

  class Meta:
    db_table = 'ticket'

class Credit_card(models.Model):
  card_number = models.CharField(max_length=255, unique=True)
  card_type = models.CharField(max_length=255)
  expiration_year = models.PositiveIntegerField()
  expiration_month = models.PositiveIntegerField()
  security_code = models.PositiveIntegerField()
  customer = models.ForeignKey(
    Customer,
    on_delete = models.CASCADE,
    db_column = 'customer_id'
  )

  class Meta:
    db_table = 'credit_card'
