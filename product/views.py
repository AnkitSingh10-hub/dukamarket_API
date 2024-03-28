from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views,generics
from rest_framework.generics import *
from rest_framework.mixins import *
from .models import Department, Category, SubCategory, Product
from rest_framework.response import Response
from .serializers import DepartmentSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer
from utils.pagination import CustomPageNumberPagination

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("-id")
    serializer_class = DepartmentSerializer
    pagination_class = CustomPageNumberPagination
    http_method_names = ['get','head','post']


class DashboardView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    
    