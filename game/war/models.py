from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='video/')

    def __str__(self):
        return self.title


class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title