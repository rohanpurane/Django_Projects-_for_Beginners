from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('new_post/', new_post, name='new_post'),
    path('update_post/<int:pk>/', update_post, name='update_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('logout/', user_logout, name='logout'),
]
