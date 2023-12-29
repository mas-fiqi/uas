# models.py
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
