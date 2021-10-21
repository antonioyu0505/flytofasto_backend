from django.http.response import JsonResponse
from django.views import View
from .models import Customer

# Create your views here.
class CustomerView(View):

  def get(self, request):
    customers = list(Customer.objects.values())
    response = {'message' : 'OK', 'customers' : customers}
    return JsonResponse(response)

  def post(self, request):
    pass

  def put(self, request):
    pass

  def delete(self, request):
    pass