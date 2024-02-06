from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from orders.models import SalesOrder


class OrderSerializer(ModelSerializer):
    products = serializers.StringRelatedField()
    # user = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')

    class Meta:
        model = SalesOrder
        fields = ['amount', 'description', 'is_exist', 'user', 'products']
