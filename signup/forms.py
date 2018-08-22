from django import forms


from .models import Album

class Postform(forms.ModelForm):
    class Meta:
        model = Album
        field = [
            'artist',
            'album_logo',

        ]

