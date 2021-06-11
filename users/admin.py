from django.contrib import admin
from .models import Customer, Shipping

# Register your models here.

admin.site.register(Customer)
admin.site.register(Shipping)