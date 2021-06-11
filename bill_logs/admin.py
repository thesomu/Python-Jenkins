from django.contrib import admin

# Register your models here.
from bill_logs.models import imported,Export
admin.site.register(Export)
admin.site.register(imported)
