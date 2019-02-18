from django.shortcuts import render
from django.http import HttpResponse

from dal import autocomplete

from .models import *
from rest_framework.decorators import api_view
from .serializers import ShowSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['get'])
def fetch_shows(request):
    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)

def index(request):
    return HttpResponse("Hello, world. You're at the shows index.")

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
