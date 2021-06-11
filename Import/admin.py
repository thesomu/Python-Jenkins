from django.contrib import admin

# Register your models here.
from .models import Companies, Import

admin.site.register(Import)
admin.site.register(Companies)
