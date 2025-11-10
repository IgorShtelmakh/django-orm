# store/models/__init__.py
from .category import Category
from .supplier import Supplier
from .product import Product
from .customer import Customer, CustomerAddress
from .order import Order, OrderItem
from .payment import Payment
from .shipment import Shipment

# Це дозволяє імпортувати моделі як: from store.models import Product
__all__ = [
    'Category',
    'Supplier',
    'Product',
    'Customer',
    'CustomerAddress',
    'Order',
    'OrderItem',
    'Payment',
    'Shipment',
]
