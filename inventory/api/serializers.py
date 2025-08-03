from rest_framework import serializers
from inventory.models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
        read_only_fields = ('created', 'updated')