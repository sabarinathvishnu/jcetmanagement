from django.db import models

# Create your models here.
class bookdb(models.Model):
    bookname = models.CharField(max_length=100,null=True,blank=True)
    authorname = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
