from djongo import models
import datetime
# Create your models here.
class Attendances(models.Model):
    EmployeeId = models.PositiveBigIntegerField()
    SuiteNumber = models.IntegerField()
    AccessDate = models.DateField(auto_now_add=True, blank=True)
    AccessTime = models.TimeField(auto_now_add=True, blank=True)
    Status = models.CharField(max_length=20)