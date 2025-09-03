from django.db import models

# Create your models here.
class food(models.models):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=100)
    price=models.FloatField(max_length=20,default=0)
    picture=models.ImageField(upload_to='images/')