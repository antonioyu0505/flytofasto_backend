from django.urls import path, re_path
from .views import FlightList, TicketDetail, TicketList, CustomerList, CityList

urlpatterns=[
  path('customers/', CustomerList.as_view()),
  re_path(r'cities/$', CityList.as_view()),
  re_path(r'flights/$', FlightList.as_view()),
  re_path(r'tickets/$', TicketList.as_view()),
  path('tickets/<int:pk>/', TicketDetail.as_view()),
]