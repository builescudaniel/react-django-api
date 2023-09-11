from django.shortcuts import render
from rest_framework import viewsets
from .models import Dashboard, Product, ToDo, Cart, News
from .serializers import DashboardSerializer, ProductSerializer, ToDoSerializer, CartSerializer, NewsSerializer

from rest_framework.pagination import PageNumberPagination

# dashboard chapter
class DashboardViewSet(viewsets.ModelViewSet):
    queryset = Dashboard.objects.all().order_by('timestamp')
    serializer_class = DashboardSerializer

# product chapter
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

# todo chapter
class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all().order_by('task')
    serializer_class = ToDoSerializer

# cart chapter
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

# news chapter
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-timestamp')
    serializer_class = NewsSerializer




