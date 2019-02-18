from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from dal import autocomplete

from .models import *
from rest_framework.decorators import api_view
from .serializers import ShowSerializer
from rest_framework.response import Response

def index(request):
    num_shows = Show.objects.all().count()
    num_recordings = Recording.objects.all().count()

    context = {
        'num_shows': num_shows,
        'num_recordings': num_recordings,
    }
    return render(request, 'index.html', context=context)
class ShowListView(generic.ListView):
    model = Show

class ShowDetailView(generic.DetailView):
    model = Show

class RecordingListView(generic.ListView):
    model = Recording

class RecordingDetailView(generic.DetailView):
    model = Recording

class ShowAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Show.objects.all()

        if self.q:
            qs = qs.filter(date__istartswith=self.q)
        return qs


class TaperAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Taper.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


class MicAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Microphone.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

# Create your API endpoints here.
@api_view(['get'])
def fetch_shows(request):
    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)