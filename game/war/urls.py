from django.urls import path
from .views import *


urlpatterns = [
    path('', StartPageView.as_view(), name='start_page'),
    path('photo/', PhotoListView.as_view(), name='photo'),
    path('audio/', AudioListView.as_view(), name='audio'),
    path('video/', VideoListView.as_view(), name='video'),
    path('about', AboutPageView.as_view(), name='about')
]