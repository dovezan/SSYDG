
from django.shortcuts import render, redirect
from .forms import SongRequestForm
from .models import SongRequest , weektostart
def song_request(request):
    if request.method == 'POST':
        form = SongRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongRequestForm()
    
    return render(request, 'songrequest/song_request.html', {'form': form})

def song_list(request):
    song_requests = SongRequest.objects.all()
    return render(request, 'songrequest/song_list.html', {'song_requests': song_requests})
def today(request):
    song_list = SongRequest.objects.order_by("timestamp")
    weektostart_value = weektostart.objects.first().week  # 获取初始的 weektostart 值

    song_groups = [song_list[i:i+4] for i in range(0, len(song_list), 4)]

    # 为每组歌曲增加周数
    for idx, song_group in enumerate(song_groups):
        for song in song_group:
            song.week = weektostart_value + idx

    content = {"song_groups": song_groups}
    return render(request, "today_list/today.html", content)
# Create your views here.
