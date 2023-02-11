from django.db import models

class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Mail(models.Model):
    name=models.CharField(max_length=100, default=None)
    to=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    body=models.CharField(max_length=1000)


class AdminResponse(models.Model):
    name=models.CharField(max_length=100, default=None)
    to=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    body=models.CharField(max_length=1000)
    response=models.CharField(max_length = 150)
    
   