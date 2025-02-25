from django.shortcuts import render, get_object_or_404
from .models import Track, Playlist

def index(request):
    tracks = Track.objects.all()
    playlists = Playlist.objects.all()
    return render(request, 'index.html', {'tracks': tracks, 'playlists': playlists})

def playlist_detail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'playlist.html', {'playlist': playlist})

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    
    # Get all tracks ordered by id (or any other ordering you prefer)
    all_tracks = Track.objects.all().order_by('id')
    
    # Find current track position
    track_ids = list(all_tracks.values_list('id', flat=True))
    current_index = track_ids.index(track.id)
    
    # Get previous and next tracks
    previous_track = all_tracks[current_index - 1] if current_index > 0 else None
    next_track = all_tracks[current_index + 1] if current_index < len(track_ids) - 1 else None
    
    context = {
        'track': track,
        'previous_track': previous_track,
        'next_track': next_track,
    }
    return render(request, 'track_detail.html', context)