from django.db import models

"""These are attributes for employee table"""


class empTable(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    designation = models.CharField(max_length=30, default='null')
    password = models.IntegerField(default=12345)
