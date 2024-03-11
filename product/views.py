from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Department, Category, SubCategory, Product
from rest_framework.response import Response
from .serializers import DepartmentSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer
# Create your views here.


class DepartmentList(ListAPIView):
    queryset = Department.objects.all().order_by("-id")
    serializer_class = DepartmentSerializer
    

class ProductList(APIView):
    def get(self, request):
        new_products = Product.objects.filter(section__name='New Products')
        featured_products = Product.objects.filter(section__name='Featured Products')
        recommended_products = Product.objects.filter(section__name='Recommended')
        serializer_new_products = ProductSerializer(new_products, many=True)
        serializer_featured_products = ProductSerializer(featured_products, many=True)
        serializer_recommended = ProductSerializer(recommended_products, many=True)
        return Response({
            "top_deals_of_the_day": serializer_new_products.data,
            "top_selling_products": serializer_featured_products.data,
            "recommended_products": serializer_recommended.data
        })
        