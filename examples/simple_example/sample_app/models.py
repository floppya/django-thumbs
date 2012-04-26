# -*- encoding: utf-8 -*-

from django.db import models
from django_thumbs.db.models import ImageWithThumbsField


class Photo(models.Model):
    title = models.CharField(max_length=140)
    image = ImageWithThumbsField(upload_to='photos', sizes=((125, 125),))
