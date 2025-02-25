from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('playlist/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('track/<int:pk>/', views.track_detail, name='track_detail'),
]