from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=255, default='name', null = False) # we added a defult and null just becouse i chande in model)
    last_name= models.CharField(max_length=255)
    email = models.CharField(max_length=255, default='email', null=False)
    password =models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

