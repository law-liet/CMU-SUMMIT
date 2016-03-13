from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length= 13)
    role = models.CharField(max_length=64)
    interested_company = models.CharField(max_length= 128)
