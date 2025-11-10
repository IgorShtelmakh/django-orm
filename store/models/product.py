# store/models/product.py
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Product(models.Model):
    """Модель товару"""
    sku = models.CharField(max_length=64, unique=True, verbose_name="Артикул")
    name = models.CharField(max_length=160, verbose_name="Назва")
    category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        related_name='products',
        verbose_name="Категорія"
    )
    default_supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name="Постачальник за замовчуванням"
    )
    list_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Ціна"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Опис")
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Знижка (%)"
    )

    class Meta:
        db_table = 'products'
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['name']

    def __str__(self):
        return f"{self.sku} - {self.name}"
