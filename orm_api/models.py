from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email =models.EmailField(max_length=255)
    address = models.TextField()
    designation = models.CharField(max_length=100)
   # department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    