from rest_framework import viewsets
from inventory.models import product
from inventory.api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer