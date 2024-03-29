"""rhcode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from shows.views import fetch_shows
from shows.views import ShowAutocomplete, TaperAutocomplete, MicAutocomplete


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', include('shows.urls')),
    path('fetch_shows/', fetch_shows),
    re_path(
        r'^show-autocomplete/$',
        ShowAutocomplete.as_view(),
        name='show-autocomplete',
    ),
    re_path(
        r'^taper-autocomplete/$',
        TaperAutocomplete.as_view(create_field='name'),
        name='taper-autocomplete',
    ),
    re_path(
        r'^mic-autocomplete/$',
        MicAutocomplete.as_view(create_field='name'),
        name='mic-autocomplete',
    ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
