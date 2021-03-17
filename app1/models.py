from django.db import models

class Music (models.Model):
    username = models.CharField(max_length=100)
    url = models.URLField()
    musicName = models.CharField(max_length=300)
    artist = models.CharField(max_length=500,blank=True,null=True)
    fa = models.TextField()
    en= models.TextField()
    fav= models.IntegerField(default=0)

    def __str__(self):
        return self.musicName


class User (models.Model):
    username = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)

    def __srt__(self):
        return self.username
