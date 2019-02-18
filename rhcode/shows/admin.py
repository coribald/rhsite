from django.contrib import admin

from .models import *
from .forms import *

class RecordingAdmin(admin.ModelAdmin):
    form = RecordingForm

admin.site.register(Show)
admin.site.register(Performance)
admin.site.register(Tour)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Recording, RecordingAdmin)
admin.site.register(RecordingType)
admin.site.register(Taper)
admin.site.register(Microphone)
admin.site.register(Venue)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Country)
