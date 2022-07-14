from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Products, Category
from core.permissions import ProductPermission
from core.serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductView(ModelViewSet):
    queryset = Products.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'price']
    permission_classes = (ProductPermission, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


