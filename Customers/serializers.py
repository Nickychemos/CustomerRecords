from rest_framework import serializers
from Customers.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
        Model = Customers
        fields = ['CustomerID', 'FirstName', 'LastName', 'Gender']