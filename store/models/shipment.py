# store/models/shipment.py
from django.db import models


class Shipment(models.Model):
    """Модель відправлення"""
    PENDING = 'pending'
    IN_TRANSIT = 'in_transit'
    DELIVERED = 'delivered'
    RETURNED = 'returned'

    SHIPMENT_STATUS_CHOICES = [
        (PENDING, 'Очікується'),
        (IN_TRANSIT, 'В дорозі'),
        (DELIVERED, 'Доставлено'),
        (RETURNED, 'Повернуто'),
    ]

    order = models.OneToOneField(
        'Order',
        on_delete=models.RESTRICT,
        related_name='shipment',
        verbose_name="Замовлення"
    )
    shipment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправлення")
    delivery_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата доставки")
    carrier = models.CharField(max_length=120, verbose_name="Перевізник")
    tracking_number = models.CharField(
        max_length=120,
        unique=True,
        verbose_name="Номер відстеження"
    )
    status = models.CharField(
        max_length=20,
        choices=SHIPMENT_STATUS_CHOICES,
        default=PENDING,
        verbose_name="Статус"
    )

    class Meta:
        db_table = 'shipments'
        verbose_name = "Відправлення"
        verbose_name_plural = "Відправлення"
        ordering = ['-shipment_date']

    def __str__(self):
        return f"Відправлення #{self.tracking_number}"
