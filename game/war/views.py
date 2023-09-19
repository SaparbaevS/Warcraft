from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from war.models import Picture, Video, Audio


class StartPageView(TemplateView):
    template_name = 'warapp/start_page.html'


class AboutPageView(TemplateView):
    template_name = 'warapp/about_page.html'


class PhotoListView(ListView):
    template_name = 'warapp/photo.html'
    model = Picture


class VideoListView(ListView):
    template_name = 'warapp/video.html'
    model = Video


class AudioListView(ListView):
    template_name = 'warapp/audio.html'
    model = Audio

