from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator


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
    ordering = ['date']

class ShowDetailView(generic.DetailView):

    model = Show
    ordered_set = Show.objects.all().order_by('date')

    def get_next(self):
        return self.get_object().get_next_by_date()

    def get_prev(self):
        return self.get_object().get_previous_by_date()
        

    def set1(self):
        s = Performance.objects.filter(show=self.get_object(), encore=0)
        ordered_set = s.order_by('set_order')
        return ordered_set

    def set2(self):
        s = Performance.objects.filter(show=self.get_object(), encore=1)
        ordered_set = s.order_by('set_order')
        return ordered_set
    
    def set3(self):
        s = Performance.objects.filter(show=self.get_object(), encore=2)
        ordered_set = s.order_by('set_order')
        return ordered_set

    def set4(self):
        s = Performance.objects.filter(show=self.get_object(), encore=3)
        ordered_set = s.order_by('set_order')
        return ordered_set

    def recordings(self):
        return Recording.objects.filter(show=self.get_object())
        

class RecordingListView(generic.ListView):
    model = Recording
    ordering = ['-show']

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