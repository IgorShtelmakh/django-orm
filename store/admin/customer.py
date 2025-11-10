# store/admin/customer.py
from django.contrib import admin
from store.models import Customer, CustomerAddress


class CustomerAddressInline(admin.TabularInline):
    """Inline для адрес клієнта"""
    model = CustomerAddress
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'orders_count']
    list_filter = ['created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering = ['last_name', 'first_name']
    inlines = [CustomerAddressInline]

    def orders_count(self, obj):
        """Кількість замовлень клієнта"""
        return obj.orders.count()
    orders_count.short_description = 'Кількість замовлень'


@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address_type', 'city', 'street', 'postal_code']
    list_filter = ['address_type', 'city', 'country']
    search_fields = ['customer__first_name', 'customer__last_name', 'city', 'street']
    ordering = ['customer', 'address_type']
