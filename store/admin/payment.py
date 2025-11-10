# store/admin/payment.py
from django.contrib import admin
from store.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'payment_date', 'amount', 'payment_method', 'status', 'transaction_id']
    list_filter = ['status', 'payment_method', 'payment_date']
    search_fields = ['order__id', 'transaction_id']
    ordering = ['-payment_date']
    readonly_fields = ['payment_date']
