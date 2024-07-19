from django.db import models
from django.db.models import Avg


class Location(models.Model):
    defaultURL = 'https://d21x6gt1bw5dh5.cloudfront.net/building1.jpg'

    location_name = models.CharField(max_length=40)
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=45)
    picture = models.URLField(blank=True, default=defaultURL)
    description = models.TextField()

    def __str__(self):
        return self.location_name

    def average_score(self):
        return self.rating_set.aggregate(Avg('number_stars'))

    def total_ratings(self):
        return self.rating_set.count()


class Rating(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    number_stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.number_stars)
