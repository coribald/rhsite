from django.contrib import admin

from .models import *
from .forms import *

class RecordingAdmin(admin.ModelAdmin):
    form = RecordingForm

class TourAdmin(admin.ModelAdmin):
    ordering = ('name',)

class VenueAdmin(admin.ModelAdmin):
    ordering = ('name',)

class CityAdmin(admin.ModelAdmin):
    ordering = ('name',)

class RegionAdmin(admin.ModelAdmin):
    ordering = ('name',)

class CountryAdmin(admin.ModelAdmin):
    ordering = ('name',)

class SongAdmin(admin.ModelAdmin):
    ordering = ('name',)

class AlbumAdmin(admin.ModelAdmin):
    ordering = ('name',)

class TaperAdmin(admin.ModelAdmin):
    ordering = ('name',)

class MicrophoneAdmin(admin.ModelAdmin):
    ordering = ('name',)

admin.site.register(Show)
admin.site.register(Performance)
admin.site.register(Tour, TourAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Recording, RecordingAdmin)
admin.site.register(RecordingType)
admin.site.register(Taper, TaperAdmin)
admin.site.register(Microphone, MicrophoneAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Country, CountryAdmin)
