from django.db import models

# Create your models here.

class Customers(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    FirstName = models.TextField(max_length=255)
    LastName = models.CharField(max_length=255)
    Gender = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}" #Helps to get a preview of the name of the customer