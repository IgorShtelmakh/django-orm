# store/models/order.py
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Order(models.Model):
    """Модель замовлення"""
    PENDING = 'pending'
    PROCESSING = 'processing'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'
    CANCELLED = 'cancelled'

    STATUS_CHOICES = [
        (PENDING, 'Очікування'),
        (PROCESSING, 'В обробці'),
        (SHIPPED, 'Відправлено'),
        (DELIVERED, 'Доставлено'),
        (CANCELLED, 'Скасовано'),
    ]

    customer = models.ForeignKey(
        'Customer',
        on_delete=models.RESTRICT,
        related_name='orders',
        verbose_name="Клієнт"
    )
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
        verbose_name="Статус"
    )
    shipping_address = models.ForeignKey(
        'CustomerAddress',
        on_delete=models.RESTRICT,
        related_name='shipping_orders',
        verbose_name="Адреса доставки"
    )
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Загальна сума"
    )

    class Meta:
        db_table = 'orders'
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ['-order_date']

    def __str__(self):
        return f"Замовлення #{self.id} від {self.customer}"


class OrderItem(models.Model):
    """Модель позиції замовлення"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Замовлення"
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.RESTRICT,
        related_name='order_items',
        verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Кількість"
    )
    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Ціна за одиницю"
    )

    class Meta:
        db_table = 'order_items'
        verbose_name = "Позиція замовлення"
        verbose_name_plural = "Позиції замовлення"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total(self):
        """Розрахунок загальної вартості позиції"""
        return self.quantity * self.unit_price
