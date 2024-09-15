from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmnin(admin.ModelAdmin):
    """
    Админка для товаров.
    """

    list_display = (
        'pk',
        'title',
        'description',
        'price',
    )
    list_filter = (
        'title',
    )
