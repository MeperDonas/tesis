from rest_framework.routers import DefaultRouter
from inventory.api.views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls