# models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='crops/')
    description = models.TextField(blank=True, null=True)
    date_planted = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animals/')
    breed = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    affected_crops = models.ManyToManyField(Crop, blank=True)
    affected_animals = models.ManyToManyField(Animal, blank=True)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"Treatment for {self.disease.name}"
