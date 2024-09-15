from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    """
    Модель продуктов.
    """

    title = models.CharField(
        max_length=100,
        verbose_name='Название')
    description = models.TextField(
        max_length=500,
        verbose_name='Описание',
        null=True, blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена')

    def __str__(self) -> str:
        return self.title

    def clean(self) -> None:
        if self.price < 0:
            raise ValidationError(
                'Цена не может быть отрицательным значением.')

    class Meta:
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
