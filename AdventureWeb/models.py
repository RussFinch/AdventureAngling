from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Gallery(models.Model):

    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='static/static_dirs/images/')
    description = models.TextField()

    def __str__(self):
        return self.title
