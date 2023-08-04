from django.db import models

# Create your models here.
class FavoriCarsModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.CharField(max_length=100)



class BestCarsModel(models.Model):
    image = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)

