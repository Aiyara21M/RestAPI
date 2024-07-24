from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50)
    dct=models.CharField(max_length=255)
    active=models.BooleanField(default=False)
