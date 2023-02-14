from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('payment_status/', payment_status, name='payment_status'),
]
