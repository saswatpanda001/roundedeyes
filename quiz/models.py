from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
import uuid
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):

    answer_choices =(
        ("1","1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name="category")
    categories = models.ManyToManyField(Category,blank=True,name="categories")
    question = models.TextField(blank=True,null=True)
    answer = models.CharField(max_length=100,blank=True,null=True)
    choice1 = models.CharField(max_length=100,blank=True,null=True)
    choice2 = models.CharField(max_length=100,blank=True,null=True)
    choice3 = models.CharField(max_length=100,blank=True,null=True)
    choice4 = models.CharField(max_length=100,blank=True,null=True)
    choices = models.CharField(max_length =50,choices=answer_choices,default=None)
    image = models.ImageField(upload_to="quiz",default = "quiz/def_quiz.png")

    def __str__(self):
        return str(self.id)