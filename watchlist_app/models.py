from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.name