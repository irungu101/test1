from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.IntegerField()
    phone_number = models.TextField()
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name
