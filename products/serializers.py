from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        print("Validated Data:", validated_data)  # Debugging line
        return super().create(validated_data)