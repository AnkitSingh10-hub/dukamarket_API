from django.contrib import admin
from .models import Department, Category, SubCategory, Product, Brand, Color, Section
# Register your models here.


admin.site.register(Department)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Section)