from django.contrib import admin
from .models import Cost,Asset

@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ['asset','description','amount','date']

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['purpose','totalamount','date']