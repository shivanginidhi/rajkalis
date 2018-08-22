from django.db import models
from django.urls import reverse
from django.views.generic import CreateView, DetailView


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('signup:details' ,kwargs={{'pk': self.pk}})

    def __str__(self):

        return self.artist+"-"+self.genre


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):

        return self.song_title


class UserSignup(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    aadhar = models.IntegerField()
    photo = models.CharField(max_length=1000)



    def __str__(self):
        return self.user_name


