from django.db import models

# Create your models here.
class pais_capital(models.Model):
    pais = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)