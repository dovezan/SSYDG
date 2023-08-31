from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.song_request, name='song_request'),
    path('list/', views.song_list, name='song_list'),
    path('',views.today,name='today')
]
