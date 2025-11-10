# store/admin/shipment.py
from django.contrib import admin
from store.models import Shipment


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'tracking_number', 'carrier', 'shipment_date', 'delivery_date', 'status']
    list_filter = ['status', 'carrier', 'shipment_date']
    search_fields = ['tracking_number', 'order__id', 'carrier']
    ordering = ['-shipment_date']
    readonly_fields = ['shipment_date']
