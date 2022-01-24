from django.db import models

# Create your models here.
class Post(models.Model):
    title       = models.CharField(max_length=64)
    text        = models.TextField()
    image       = models.ImageField(upload_to = 'blogs/static/images/blogImages', blank = True)
    featured    = models.BooleanField(default=False)