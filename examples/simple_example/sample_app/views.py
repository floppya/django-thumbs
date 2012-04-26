# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from sample_app.models import Photo


def index(request):
    photos = Photo.objects.all()
    return render_to_response('index.html', {'photos': photos})


def show_img(request, id_img):
    photo = get_object_or_404(Photo, pk=id_img)
    return render_to_response('show_img.html', {'photo': photo})
