from django.db import models

# Create your models here.
class Export(models.Model):
    billing_amt=models.IntegerField()
    date_of_export=models.CharField(max_length=20)
    gst_imposed=models.CharField(max_length=20)
    exported_to=models.CharField(max_length=20)
    order_ID=models.IntegerField()
    quantity=models.IntegerField()
    estimated_time=models.CharField(max_length=50)

class imported(models.Model):
    billing_amt=models.IntegerField()
    date_of_import=models.CharField(max_length=20)
    gst_imposed=models.CharField(max_length=20)
    imported_from=models.CharField(max_length=20)
    order_ID=models.IntegerField()
    quantity=models.IntegerField()
    estimated_time=models.CharField(max_length=50)   


