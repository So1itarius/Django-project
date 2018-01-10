from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')

class Test(models.Model):
    title = models.TextField(max_length=50, verbose_name='title',primary_key=True)
    price = models.TextField(max_length=20, verbose_name='price')
