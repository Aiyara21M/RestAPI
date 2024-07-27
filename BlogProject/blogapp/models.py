from django.db import models


class Category(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self) :
        return self.name
    

class Blog(models.Model):
    title=models.CharField(max_length=50)
    dct=models.CharField(max_length=255)
    active=models.BooleanField(default=True)
    category =  models.ForeignKey(Category,on_delete=models.CASCADE,default=None)


