# store/admin/supplier.py
from django.contrib import admin
from store.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'email', 'products_count']
    search_fields = ['name', 'email', 'phone']
    ordering = ['name']

    def products_count(self, obj):
        """Кількість товарів від постачальника"""
        return obj.products.count()
    products_count.short_description = 'Кількість товарів'
