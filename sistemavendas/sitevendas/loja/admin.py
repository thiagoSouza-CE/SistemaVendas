from django.contrib import admin

from .models import Product, Stock, Order, ItemOrder, Perfil, Invoice

admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(ItemOrder)
admin.site.register(Perfil)
admin.site.register(Invoice)