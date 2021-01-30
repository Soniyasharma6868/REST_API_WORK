from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)


class Staff(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    city=models.CharField(max_length=100)


class Employee(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    city=models.CharField(max_length=100)