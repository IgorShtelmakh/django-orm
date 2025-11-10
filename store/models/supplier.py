# store/models/supplier.py
from django.db import models


class Supplier(models.Model):
    """Модель постачальника"""
    name = models.CharField(max_length=120, unique=True, verbose_name="Назва")
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name="Телефон")
    email = models.EmailField(max_length=150, null=True, blank=True, verbose_name="Email")

    class Meta:
        db_table = 'suppliers'
        verbose_name = "Постачальник"
        verbose_name_plural = "Постачальники"
        ordering = ['name']

    def __str__(self):
        return self.name
