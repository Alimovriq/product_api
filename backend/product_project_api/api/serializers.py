from rest_framework import serializers

from core.models import Product


class ProductSerializer(serializers.Serializer):
    """
    Сериализатор данных модели продуктов.
    """

    id = serializers.IntegerField(
        read_only=True)
    title = serializers.CharField(
        required=True,
        max_length=100)
    description = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=500,
        style={'base_template': 'textarea.html'})
    price = serializers.DecimalField(
        required=True,
        max_digits=10,
        decimal_places=2)

    def create(self, validated_data):
        """
        Метод для создания объекта.
        """

        return Product.objects.create(**validated_data)

    def validate_price(self, value):
        """
        Проверка цены на отрицательное число.
        """

        if value < 0:
            raise serializers.ValidationError(
                'Значение не должно быть отрицательным числом')
        return value
