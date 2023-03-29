from musics.helper import get_audio_length
from django.db import models
from .validators import validate_is_audio

class Music(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    artiste=models.CharField(max_length=500)
    album=models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
    time_length=models.DecimalField(max_digits=20, decimal_places=2,blank=True)
    audio_file=models.FileField(upload_to='musics/')
    cover_image=models.ImageField(upload_to='music_images/')

    def save(self,*args, **kwargs):
        if not self.time_length:
            # logic for getting length of audio
            audio_length=get_audio_length(self.audio_file)
            self.time_length =f'{audio_length:.2f}'

        return super().save(*args, **kwargs)

    class META:
        ordering="id"


class Album(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=400)

class Contacts(models.Model):
    email=models.EmailField(primary_key=True)
    name=models.CharField(max_length=400)
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True, blank = True)

class AboutUs(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=400)
    description=models.TextField()
    image=models.ImageField(upload_to='about_us_images/')