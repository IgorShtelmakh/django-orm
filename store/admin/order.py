# store/admin/order.py
from django.contrib import admin
from store.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Inline для позицій замовлення"""
    model = OrderItem
    extra = 1
    readonly_fields = ['get_item_total']

    def get_item_total(self, obj):
        """Загальна вартість позиції"""
        if obj.id:
            return f"{obj.get_total()} грн"
        return "-"
    get_item_total.short_description = 'Загальна вартість'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order_date', 'status', 'total_amount', 'items_count']
    list_filter = ['status', 'order_date']
    search_fields = ['customer__first_name', 'customer__last_name', 'customer__email']
    ordering = ['-order_date']
    readonly_fields = ['order_date']
    inlines = [OrderItemInline]

    def items_count(self, obj):
        """Кількість позицій у замовленні"""
        return obj.items.count()
    items_count.short_description = 'Кількість позицій'
