from django import forms
from .models import SongRequest

class SongRequestForm(forms.ModelForm):
    class Meta:
        model = SongRequest
        fields = ['song', 'artist']
