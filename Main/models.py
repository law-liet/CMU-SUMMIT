from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length= 64)
    role = models.CharField(max_length=64)
    degree = models.CharField(max_length=64, default='none')
    major = models.CharField(max_length=64, default='none')
    department = models.CharField(max_length=128, default='none')
    institution = models.CharField(max_length=128, default='none')

class Applicant(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    major = models.CharField(max_length=64)
    university = models.CharField(max_length=128)
    graduate_time = models.DateField()
    interested_company = models.CharField(max_length=128)
    resume = models.FileField(upload_to='', default=None)