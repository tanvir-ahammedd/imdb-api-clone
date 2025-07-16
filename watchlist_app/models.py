from django.db import models

# Create your models here.
class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=300)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name

#One platform can have many movies
class WatchList(models.Model):
    name = models.CharField(max_length=50)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name