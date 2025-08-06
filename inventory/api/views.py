from rest_framework import viewsets, permissions
from inventory.models import product
from inventory.api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    permission_classes = [permissions.AllowAny] # Change to IsAuthenticated for authenticated access
    serializer_class = ProductSerializer

