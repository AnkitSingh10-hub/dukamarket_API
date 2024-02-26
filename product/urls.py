from django.urls import path, include
from .views import *

urlpatterns = [
    path('departments/', DepartmentList.as_view(),name="departments"),
    path('products/', ProductList.as_view(), name="products"),
]
