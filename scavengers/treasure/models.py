from django.db import models

# Create your models here.

class treasure(models.Model):
    treasure_name = models.CharField(max_length=200)
    treasure_description = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    hint = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)