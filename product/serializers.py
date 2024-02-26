from .models import Department, Category, SubCategory, Product, User
from rest_framework import serializers, exceptions



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']
       
        
class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    color = serializers.StringRelatedField(read_only=True)
    section = serializers.StringRelatedField(read_only=True)
    

    class Meta:
        model = Product
        fields = "__all__"