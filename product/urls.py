from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (DepartmentViewSet, ProductCountView)

router = SimpleRouter()

router.register("departments", DepartmentViewSet, basename="departments")
router.register("products", DashboardView, basename="products")

