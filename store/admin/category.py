# store/admin/category.py
from django.contrib import admin
from store.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent', 'products_count']
    list_filter = ['parent']
    search_fields = ['name']
    ordering = ['name']

    def products_count(self, obj):
        """Кількість товарів у категорії"""
        return obj.products.count()
    products_count.short_description = 'Кількість товарів'
