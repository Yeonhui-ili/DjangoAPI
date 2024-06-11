from rest_framework import serializers
from .models import Product_for_viewset

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_for_viewset
        fields = ['id', 'name', 'description', 'price', 'in_stock']
