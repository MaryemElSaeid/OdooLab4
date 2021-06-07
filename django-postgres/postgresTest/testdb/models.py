from django.db import models


class Itinew(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    
    