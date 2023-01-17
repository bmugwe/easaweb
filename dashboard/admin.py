from ast import Or
from django.contrib import admin
from .models import Order, Product
from django.contrib.auth.models import Group

admin.site.site_header = 'Base App Homepage'

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name', 'category', 'quantity')
    list_filter = ['category']

class OrderAdmin(admin.ModelAdmin):
    list_display=('product', 'staff', 'order_quantity')
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order,OrderAdmin)
# admin.site.unregister(Group)