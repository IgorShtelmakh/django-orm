# store/admin/__init__.py
from django.contrib import admin

# Імпортуємо всі admin класи
from .category import CategoryAdmin
from .supplier import SupplierAdmin
from .product import ProductAdmin
from .customer import CustomerAdmin, CustomerAddressAdmin
from .order import OrderAdmin, OrderItemInline
from .payment import PaymentAdmin
from .shipment import ShipmentAdmin

# Налаштування заголовків адмін-панелі
admin.site.site_header = "Адміністрування інтернет-магазину"
admin.site.site_title = "Shop Admin"
admin.site.index_title = "Панель управління"
