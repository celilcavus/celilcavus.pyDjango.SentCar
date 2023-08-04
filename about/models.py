from django.db import models

# Create your models here.
class AboutModel(models.Model):
    title = models.CharField(max_length=50)
    deescription = models.TextField(max_length=500)
    image = models.CharField(max_length=100)
    