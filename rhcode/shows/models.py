from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Show(models.Model):
    show_date = models.DateField(default=date.today)
    venue = models.CharField(max_length=100, default="")

#Table of all performances of all songs, to link from songs to shows and add performance info per song
class Performance(models.Model):
    song = models.ForeignKey('Song', on_delete=models.SET_NULL, null=True)
    show = models.ForeignKey('Show', on_delete=models.SET_NULL, null=True)
    set_order = models.IntegerField()
    encore = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.song_name

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    def __str__(self):
        return self.album_name

class Recording(models.Model):
    recording_name = models.CharField(max_length=100)
    recorded_show = models.ForeignKey('Show', on_delete=models.SET_NULL, null=True)
    recording_type = models.ForeignKey('RecordingTypes', on_delete=models.SET_NULL, null=True)

class RecordingTypes(models.Model):
    type_name = models.CharField(max_length=20)
    recordings = models.ForeignKey('Recording', on_delete=models.SET_NULL, null=True)
