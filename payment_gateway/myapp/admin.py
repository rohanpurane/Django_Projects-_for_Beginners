from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ColdCoffee)
class ColdCoffeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount','order_id','razorpay_payment_id','paid']