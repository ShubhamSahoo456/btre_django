from django.db import models
from listings.models import Listings

# Create your models here.


class Contacts (models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name
