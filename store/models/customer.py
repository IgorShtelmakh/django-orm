# store/models/customer.py
from django.db import models


class Customer(models.Model):
    """Модель клієнта"""
    first_name = models.CharField(max_length=120, verbose_name="Ім'я")
    last_name = models.CharField(max_length=120, verbose_name="Прізвище")
    email = models.EmailField(max_length=150, unique=True, verbose_name="Email")
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата реєстрації")

    class Meta:
        db_table = 'customers'
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CustomerAddress(models.Model):
    """Модель адреси клієнта"""
    SHIPPING = 'shipping'
    BILLING = 'billing'

    ADDRESS_TYPE_CHOICES = [
        (SHIPPING, 'Адреса доставки'),
        (BILLING, 'Адреса для рахунку'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name="Клієнт"
    )
    address_type = models.CharField(
        max_length=20,
        choices=ADDRESS_TYPE_CHOICES,
        verbose_name="Тип адреси"
    )
    street = models.CharField(max_length=255, verbose_name="Вулиця")
    city = models.CharField(max_length=120, verbose_name="Місто")
    postal_code = models.CharField(max_length=20, verbose_name="Поштовий індекс")
    country = models.CharField(max_length=120, default='Україна', verbose_name="Країна")

    class Meta:
        db_table = 'customer_addresses'
        verbose_name = "Адреса клієнта"
        verbose_name_plural = "Адреси клієнтів"
        ordering = ['customer', 'address_type']

    def __str__(self):
        return f"{self.customer} - {self.city}, {self.street}"
