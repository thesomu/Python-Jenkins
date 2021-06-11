from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.


class Import(models.Model):
    """
    Import model class that describe the different fields needed
    in import table.
    """
    different_import_status = [
        ('No', 'Pending'),
        ('Yes', 'Completed'),
    ]

    orderImport_id = models.IntegerField()
    order_date = models.DateField()
    import_product = models.CharField(max_length=20)
    orderImport_country = models.CharField(max_length=20)
    status_of_import = models.CharField(
        max_length=10, choices=different_import_status)
    total_cost = models.FloatField(max_length=20)


class Companies(models.Model):
    """
    Company model class that provide details of the various companies 
    that provide goods to the store.
    """
    product_name = models.ForeignKey(
        Import, max_length=20, on_delete=DO_NOTHING)
    company_id = models.IntegerField()
    company_name = models.CharField(max_length=20)
    price_per_piece = models.FloatField(max_length=20)
    shipping_cost = models.FloatField(max_length=20)
    estimated_dateOfDelivery = models.DateField()
