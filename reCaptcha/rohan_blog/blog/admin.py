from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'about_img', 'title', 'description')

@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'your_email', 'subject')
