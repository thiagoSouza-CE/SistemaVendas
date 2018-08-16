from django.contrib import admin

from .models import Product, Stock

admin.site.register(Product)
admin.site.register(Stock)