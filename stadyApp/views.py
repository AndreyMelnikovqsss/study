# views.py

from rest_framework import viewsets
from .models import Product, Lesson
from .serializers import ProductSerializer, LessonSerializer, ProductDetailSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        serializer = ProductDetailSerializer(self.queryset, many=True)
        return Response(serializer.data)
