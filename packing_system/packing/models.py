from django.db import models

# Create your models here.

class Furniture(models.Model):
    name = models.CharField()
    img = models.ImageField(upload_to='packing')
    Group = models.ForeignKey('Group', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.SlugField(max_length=15,unique=True)

    def __str__(self):
        return self.name