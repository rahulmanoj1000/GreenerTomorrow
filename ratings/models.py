from django.db import models

# Create your models here.
class Ratings(models.Model):
    rating = models.IntegerField(null=False)