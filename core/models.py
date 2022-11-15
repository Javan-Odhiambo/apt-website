from django.db import models

# Create your models here.

class Testimony(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    testimony_text = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='images/', null=True, verbose_name="")
    is_approved = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now=True)
    
    def  __str__(self):
        return self.testimony_text
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=400)
    
class Email(models.Model):
    email = models.EmailField(max_length=254, unique=True)
