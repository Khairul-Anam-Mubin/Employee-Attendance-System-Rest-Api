from djongo import models

# Create your models here.
class Employees(models.Model):
    EmployeeId = models.PositiveBigIntegerField(primary_key=True, unique=True)
    EmployeeFirstName = models.CharField(max_length=100)
    EmployeeLastName = models.CharField(max_length=100)
    EmployeeDesignation = models.CharField(max_length=100)
    EmployeeAddress = models.CharField(max_length=200)
    EmployeePhoneNumber = models.CharField(max_length=15)
    EmployeeEmail = models.EmailField(max_length=100)
    EmployeePin = models.CharField(max_length=100)
    EmployeeRole = models.CharField(max_length=100)