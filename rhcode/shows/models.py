from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Show(models.Model):
    date = models.DateField(default=date.today)
    venue = models.CharField(max_length=40, default="")
    city = models.CharField(max_length=40, default="")
    state = models.CharField(max_length=40, default="")
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, blank=True, null=True)
    tour = models.ForeignKey('Tour', on_delete=models.SET_NULL, blank=True, null=True)
    sfm_setlist_id = models.CharField(max_length=15, default="00000000")
    notes = models.CharField(max_length=250, default="")
        
    def __str__(self):
        retstr = str(self.date) + ' - ' + str(self.venue) + ', ' + str(self.city) + ', ' + str(self.country)
        return retstr

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
    notes = models.CharField(max_length=250, default="")

class Tour(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=100)
    track_number = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1)
        ]
    )
    song = models.ForeignKey('Song', on_delete=models.SET_NULL, null=True)

class Album(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Release(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField(default=date.today)
    parent_album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Recording(models.Model):
    name = models.CharField(max_length=100)
    recorded_show = models.ForeignKey('Show', on_delete=models.SET_NULL, null=True)
    recording_type = models.ForeignKey('RecordingType', on_delete=models.SET_NULL, null=True)

class RecordingType(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    def __str__(self):
        return self.name