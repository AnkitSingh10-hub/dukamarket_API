from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.mixins import *
from .models import Department, Category, SubCategory, Product
from rest_framework.response import Response
from .serializers import DepartmentSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer
# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by("-id")
    serializer_class = DepartmentSerializer
    http_method_names = ['get','head','post']

