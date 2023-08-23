from django.contrib import admin

from .models import Category, Size, Product, Order

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Order)

