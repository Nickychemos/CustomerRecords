from rest_framework import viewsets
from .models import Customers
from .serializers import CustomerSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
   queryset = Customers.objects.all()
   serializer_class = CustomerSerializer