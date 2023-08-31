
from django.db import models

class SongRequest(models.Model):
    song = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song} by {self.artist}"
class weektostart(models.Model):
    week = models.IntegerField()

    def __str__(self):
        return f"{self.week}"
# Create your models here.
