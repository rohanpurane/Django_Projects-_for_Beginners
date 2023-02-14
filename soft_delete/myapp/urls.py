from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('deleted_items/', deleted_items, name='deleted_items'),
    path('soft_del/<int:pk>/', soft_del, name='soft_del'),
    path('permanent_delete/<int:pk>/', permanent_delete, name='permanent_delete'),
    path('restore_data/<int:pk>/', restore_data, name='restore_data'),
]