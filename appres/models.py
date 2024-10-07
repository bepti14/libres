from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Student(models.Model):
    id = models.SmallAutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    division = models.CharField(max_length=4)
    di_nmb = models.SmallIntegerField()

class Teacher(models.Model):
    id = models.SmallAutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    pupils = models.CharField(max_length=4)

class Grade(models.Model):
    id = models.SmallAutoField(primary_key=True)
    mark = models.SmallIntegerField(validators=[MaxValueValidator(6), MinValueValidator(1)])
    weight = models.SmallIntegerField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40)
