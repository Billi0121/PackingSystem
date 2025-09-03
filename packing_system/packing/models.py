from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.SlugField(max_length=15,unique=True)

    def __str__(self):
        return self.name
    
