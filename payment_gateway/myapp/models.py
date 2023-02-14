from django.db import models

# Create your models here.

class ColdCoffee(models.Model):
    name = models.CharField(max_length=70)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)