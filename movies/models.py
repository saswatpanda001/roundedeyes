from pyexpat import model
from django.db import models
import uuid
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name



class Movies(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(blank=True, null=True)
    director = models.CharField(max_length=200,blank=True,null=True)
    image = models.ImageField(upload_to="movies",default="movies.def_movie.png",blank=True,null=True)

    def __str__(self):
        return self.name



    
    