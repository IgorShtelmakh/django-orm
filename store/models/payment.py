# store/models/payment.py
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Payment(models.Model):
    """Модель платежу"""
    CASH = 'cash'
    CARD = 'card'
    BANK_TRANSFER = 'bank_transfer'
    ONLINE = 'online'

    PAYMENT_METHOD_CHOICES = [
        (CASH, 'Готівка'),
        (CARD, 'Карткою'),
        (BANK_TRANSFER, 'Банківський переказ'),
        (ONLINE, 'Онлайн оплата'),
    ]

    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'
    REFUNDED = 'refunded'

    PAYMENT_STATUS_CHOICES = [
        (PENDING, 'Очікується'),
        (COMPLETED, 'Завершено'),
        (FAILED, 'Не вдалося'),
        (REFUNDED, 'Повернено'),
    ]

    order = models.ForeignKey(
        'Order',
        on_delete=models.RESTRICT,
        related_name='payments',
        verbose_name="Замовлення"
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата платежу")
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Сума"
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        verbose_name="Спосіб оплати"
    )
    status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default=PENDING,
        verbose_name="Статус"
    )
    transaction_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="ID транзакції"
    )

    class Meta:
        db_table = 'payments'
        verbose_name = "Платіж"
        verbose_name_plural = "Платежі"
        ordering = ['-payment_date']

    def __str__(self):
        return f"Платіж #{self.id} на суму {self.amount} грн"
