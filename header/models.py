from django.db import models
from django.forms import CharField

# Create your models here.
class Header(models.Model):
    name = models.CharField(max_length=32)
    show = models.BooleanField(default = False)