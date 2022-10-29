from email.policy import default
from django.db import models

# Create your models here.


class Category(models.Model):
    title=models.CharField( max_length=200,null=True,blank=True)

    def __str__(self):
        return self.title
    


class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,default=None)
    title=models.CharField( max_length=200,null=True,blank=True)
    desc=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.title