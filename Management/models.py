from django.db import models
from Employee.models import empTable

class dailyAttendance(models.Model):
    empId = models.ForeignKey(empTable, on_delete=models.CASCADE)
    inTime = models.CharField(max_length=20, default='null')
    outTime = models.CharField(max_length=20, default='null')


class empAttendance(models.Model):
    empId = models.ForeignKey(empTable, on_delete=models.CASCADE)
    dayOne = models.FloatField(default=0)
    dayTwo = models.FloatField(default=0)
    dayThree = models.FloatField(default=0)
    dayFour = models.FloatField(default=0)
    dayFive = models.FloatField(default=0)
    daySix = models.FloatField(default=0)
    daySeven = models.FloatField(default=0)
    dayEight = models.FloatField(default=0)
    dayNine = models.FloatField(default=0)
    dayTen = models.FloatField(default=0)


class totalAttendance(models.Model):
    empId = models.ForeignKey(empTable, on_delete=models.CASCADE)
    May = models.FloatField(default=0)
    June = models.FloatField(default=0)
    July = models.FloatField(default=0)
