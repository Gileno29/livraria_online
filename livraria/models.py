from django.db import models

# Create your models here.
class Book(models.Model):
    titulo= models.CharField(max_length=300)
    categoria= models.CharField(max_length=200)
    data_publicacao=models.DateTimeField()
    valor= models.FloatField()
    sinopse= models.CharField(max_length=800)


class Author(models.Model):
    nome = models.CharField(max_length=200)



class Carrinho(models.Model):
    item= models.CharField(max_length=300)
    data_add= models.DateTimeField(auto_now=True)
    comprado=models.BooleanField(default=False)


class Compra(models.Model):
    data_compra=models.DateTimeField(auto_now=True)
    valor= models.FloatField()
