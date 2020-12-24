from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Admin, Customer, Category, Product, Cart, CartProduct, Order, ProductImage])