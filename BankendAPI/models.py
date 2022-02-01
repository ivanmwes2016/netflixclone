from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, unique= True)
    descr = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    imageTitle = models.CharField(max_length=100)
    trailer = models.BooleanField()
    video = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    isSeries = models.BooleanField()


# Movie list Model
