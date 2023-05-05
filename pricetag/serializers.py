from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.Serializer):
    title_product = serializers.CharField(max_length=120)
    descr_product = serializers.CharField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)