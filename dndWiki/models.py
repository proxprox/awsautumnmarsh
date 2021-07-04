from django.db import models

# Create your models here.

class Monster(models.Model):
    name = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=200,null=True)
    description = models.TextField(default="Enter Description here")
    class Meta:
        ordering = ('type',)
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=200,null=True)
    race = models.CharField(max_length=200,null=True)
    description = models.TextField(default="Enter Description here")
    def __str__(self):
        return self.name

class Recap(models.Model):
    date = models.CharField(max_length=200,null=True)
    description = models.TextField(default="Enter Description here")
    def __str__(self):
        return self.date

class Item(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.name


