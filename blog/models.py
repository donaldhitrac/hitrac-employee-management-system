from django.db import models

class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=20)

    class Meta:
        db_table = "Employee"