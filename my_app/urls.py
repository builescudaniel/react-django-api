from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'dashboard', views.DashboardViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'todo', views.ToDoViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
