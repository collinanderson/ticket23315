from django.db import models

# Create your models here.
class Address(models.Model):
    country = models.ForeignKey('b.DeliveryCountry')

class Person(models.Model):
    pass
