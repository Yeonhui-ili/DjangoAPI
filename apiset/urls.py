from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# ViewSet에서 제공하는 모든 액션에 대해 URL 경로를 자동으로 생성
router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]