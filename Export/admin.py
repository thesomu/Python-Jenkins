from django.contrib import admin

# Register your models here.
from .models import Export, Client_Demand

admin.site.register(Export)
admin.site.register(Client_Demand)