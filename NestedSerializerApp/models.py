from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='sungby')
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.title
