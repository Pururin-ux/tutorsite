from django.db import models

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.FloatField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

