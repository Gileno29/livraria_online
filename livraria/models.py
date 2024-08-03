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
    
