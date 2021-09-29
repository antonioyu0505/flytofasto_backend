from django.db import models

class Location(models.Model):
  name = models.CharField(max_length=255)
  level = models.IntegerField()
  level_reference = models.IntegerField(blank=True, null=True)

  class Meta:
    db_table = 'location'

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
  location_to = models.ForeignKey(
    Location, 
    on_delete = models.CASCADE,
    related_name = 'location_id_to',
    db_column = 'location_id_to'
  )
  location_from = models.ForeignKey(
    Location, 
    on_delete = models.CASCADE,
    related_name = 'location_id_from',
    db_column = 'location_id_from'
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
