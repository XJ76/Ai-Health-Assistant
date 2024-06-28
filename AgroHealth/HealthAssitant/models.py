# Create your models here.
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crops/')
    # other fields as needed

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animals/')
    # other fields as needed

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    # other fields as needed

    def __str__(self):
        return self.name

class Treatment(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    description = models.TextField()
    # other fields as needed

    def __str__(self):
        return f"Treatment for {self.disease.name}"
