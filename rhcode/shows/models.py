from django.db import models
from django.urls import reverse
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Show(models.Model):
    date = models.DateField(default=date.today)
    venue = models.ForeignKey('Venue', on_delete=models.SET_NULL, blank=True, null=True)
    tour = models.ForeignKey('Tour', on_delete=models.SET_NULL, blank=True, null=True)
    sfm_setlist_id = models.CharField(max_length=15, default="00000000")
    notes = models.CharField(max_length=250, default="")
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('show-detail', args=[str(self.id)])
    def __str__(self):
        retstr = str(self.date) + ' - ' + str(self.venue)
        return retstr

# Table of all performances of all songs, to link from songs to shows and add performance info per song
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
    def __str__(self):
        retstr = str(self.show.date) + " - " + self.song.name
        return retstr

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
    show = models.ForeignKey('Show', on_delete=models.SET_NULL, null=True)
    recording_type = models.ForeignKey('RecordingType', on_delete=models.SET_NULL, null=True)
    mic = models.ForeignKey('Microphone', on_delete=models.SET_NULL, null=True)
    taper = models.ForeignKey('Taper', on_delete=models.SET_NULL, null=True)
    source1 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='matrix_source1')
    source2 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='matrix_source2')
    source3 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='matrix_source3')
    notes = models.CharField(max_length=500, default="")
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('recording-detail', args=[str(self.id)])
    def __str__(self):
        if str(self.recording_type) == "Audience":
            retstr = str(self.show) + " - " + str(self.mic) + " by " + str(self.taper)
        elif str(self.recording_type) == "Matrix":
            retstr = str(self.show) + " - " + str(self.recording_type) + " by " + str(self.taper)

        else:
            retstr = str(self.show) + " - " + str(self.recording_type) + " (" + str(self.mic) + ") by " + str(self.taper)
        return retstr

class RecordingType(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Microphone(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Taper(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=80)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=80)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=80)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    def __str__(self):
        return self.name