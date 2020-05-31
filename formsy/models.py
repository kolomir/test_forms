from django.db import models
from datetime import datetime


class Tools(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=60)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Rental(models.Model):
    tools = models.ForeignKey(Tools, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date_of_rent = models.DateTimeField('Date of rent', default=datetime.now())
    date_of_return = models.DateTimeField('Date of return')

    def __str__(self):
        return self.tools