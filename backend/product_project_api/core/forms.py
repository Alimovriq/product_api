from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    """
    Форма для товаров.
    """

    class Meta:
        model = Product
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'price': 'Цена'
        }
        help_texts = {
            'title': 'Указать название товара (Обязательное поле)',
            'description': 'Указать описание товара (Необязательное поле)',
            'price': 'Указать цену товара (Обязательное поле)'
        }
        fields = ['title', 'description', 'price']
