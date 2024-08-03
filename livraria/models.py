from django.db import models

# Create your models here.

class Carrinho(models.Model):
    item= models.CharField(max_length=300)
    data_add= models.DateTimeField(auto_now=True)
    comprado=models.BooleanField(default=False)


class Compra(models.Model):
    data_compra=models.DateTimeField(auto_now=True)
    valor= models.FloatField()
