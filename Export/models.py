from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class Client_Demand(models.Model):
    """
    """
    client_id = models.IntegerField()
    product_name = models.CharField(max_length=40)
    client_name = models.CharField(max_length=50)
    client_address = models.CharField(max_length=100)
    client_country = models.CharField(max_length=30)
    quantity_demanded = models.IntegerField()


class Export(models.Model):
    """
    Export model class which describes the fields needed for
    export table.Contains all the details that are required at the time
    of product export.
    """
    different_export_status = [
        ('No', 'Pending'),
        ('Yes', 'Completed'),
    ]
    exportProduct_id = models.IntegerField()
    product_name = models.ForeignKey(
        Client_Demand, max_length=30, on_delete=DO_NOTHING)
    client_name = models.CharField(max_length=50)
    price_per_piece = models.FloatField()
    date_of_export = models.DateField()
    status = models.CharField(max_length=20, choices=different_export_status)
