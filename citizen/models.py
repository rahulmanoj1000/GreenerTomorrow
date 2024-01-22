from django.db import models

# Create your models here.
class CitizenInput(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField()
    image = models.ImageField()
    address = models.TextField(null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    input_date = models.DateField(null=True)