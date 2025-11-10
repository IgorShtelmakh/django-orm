# store/admin/product.py
from django.contrib import admin
from django.utils.html import format_html
from store.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'sku', 'name', 'category', 'default_supplier', 'list_price', 'discount', 'price_colored']
    list_filter = ['category', 'default_supplier']
    search_fields = ['sku', 'name', 'description']
    ordering = ['name']
    list_per_page = 20

    def price_colored(self, obj):
        """Відображення ціни з кольоровим індикатором"""
        if obj.list_price:
            if obj.list_price > 40000:
                color = 'red'
            elif obj.list_price > 20000:
                color = 'orange'
            else:
                color = 'green'
            return format_html(
                '<span style="color: {};"><b>{} грн</b></span>',
                color,
                obj.list_price
            )
        return '-'
    price_colored.short_description = 'Ціна (кольорова)'
