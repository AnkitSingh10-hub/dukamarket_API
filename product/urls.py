from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (DepartmentViewSet, DashboardView)

router = SimpleRouter()

router.register("departments", DepartmentViewSet, basename="departments")
router.register("dashboard", DashboardView, basename="dashboard")

