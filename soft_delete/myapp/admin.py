from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(XYZ_Shop)
class XYZ_ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'qty', 'price']