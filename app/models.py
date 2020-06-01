# -*- coding: utf-8 -*-
from django.db import models
from django.db import models

# Create your models here.


class Paintings(models.Model):
    name = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=100, null=True)
    artist = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True, upload_to='documents/')
    description = models.CharField(max_length=500, null=True)

