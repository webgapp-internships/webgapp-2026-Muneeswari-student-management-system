from django.db import models

# Create your models here.

class Forms(models.Model):
    name = models.CharField(max_length=20, default='')
    age = models.IntegerField(default=0)
    dob = models.DateField(blank=True, null=True)
    regno = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    gender = models.CharField(max_length=10, default='')
    skills = models.CharField(max_length=50)
    year = models.CharField(max_length=20, default='')