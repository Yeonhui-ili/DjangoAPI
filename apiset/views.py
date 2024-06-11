from rest_framework import viewsets
from .models import Product_for_viewset
from .serializers import ProductSerializer

# ModelViewSet을 사용하여 CRUD 작업을 자동화( list, create, retrieve, update, partial_update, destroy 등이 제공됨)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product_for_viewset.objects.all()
    serializer_class = ProductSerializer
