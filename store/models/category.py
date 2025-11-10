# store/models/category.py
from django.db import models


class Category(models.Model):
    """Модель категорії товарів"""
    name = models.CharField(max_length=120, unique=True, verbose_name="Назва")
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name="Батьківська категорія"
    )

    class Meta:
        db_table = 'categories'
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

    def __str__(self):
        return self.name
