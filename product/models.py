from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from datetime import datetime


class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    
    
class Category(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.department.name} --> {self.name}"



class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.category.department.name} --> {self.category.name} --> {self.name}"



class ProductStatus(models.TextChoices):
    BRANDNEW = "Brand New", "Brand New"
    RECENTLYUSED = "Recently Used", "Recently Used"
    USED = "Used", "Used"
    OLD = "Old", "Old"



    
class SectionType(models.TextChoices):
    NEWPRODUCTS = "New Products", "New Products"    
    FEATUREDPRODUCTS = "Featured Products", "Featured Products"    
    RECOMMENDED = "Recommended", "Recommended"    
    

    
class Section(models.Model):
    name = models.CharField(max_length=200, choices=SectionType.choices)

    def __str__(self):
        return self.name


    
class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name



class Color(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.code



class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(default='', max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    product_details = models.TextField()
    description = models.TextField()
    total_availability = models.IntegerField()
    featured_image = models.CharField(max_length=200)
    tags = models.CharField(max_length=50)
    price = models.IntegerField()
    product_status = models.CharField(
        max_length=50,
        choices=ProductStatus.choices,
        default=ProductStatus.BRANDNEW,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, null=True, blank=True)

    
    def __str__(self) -> str:
        return f"{self.product_name}"
    


def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, Product)
    