from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class AboutMe(models.Model):
    about_img = models.ImageField(upload_to='about_img',null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

class ContactMe(models.Model):
    fullname = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=100)
    subject = models.TextField()