from django.db import models
import uuid
# Create your models here.

class Images(models.Model):
    url = models.TextField()
    class Meta:
        ordering = ["url"]
    def __str__(self):
        return self.url


class Location(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    description = models.TextField()
    name = models.TextField()
    city = models.TextField()
    images = models.ManyToManyField(Images,blank=True)

class LocationImages(models.Model):
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True)
    location = models.ForeignKey(Location, related_name='+', on_delete=models.CASCADE)
    url = models.TextField()
