from django.db import models

# Create your models here.
class APackage(models.Model):
    delivery_person = models.ForeignKey('a.Person')

class DeliveryCountry(models.Model):
    pass
