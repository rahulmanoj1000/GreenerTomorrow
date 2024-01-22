from django.db import models
# Create your models here.

class Progress(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to='progress_images/')
    address = models.TextField(null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    input_date = models.DateField(null=True)

    def __str__(self):
        return self.name
    
class WorkMan(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Pre_completed(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to='progress_images/')
    address = models.TextField(null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    input_date = models.DateField(null=True)

    def __str__(self):
        return self.name
    
class Completed(models.Model):
    sent_id = models.IntegerField()
    image = models.ImageField(upload_to='progress_images/')
    