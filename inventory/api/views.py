from rest_framework import viewsets
from inventory.models import Product
from inventory.api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer