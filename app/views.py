from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.

def home(request):
    images = Image.objects.all()   

    context = {
        'images':images
    }

    return render(request, 'home.html', context)

def image(request, image_id):

    try:
        image = Image.objects.get( id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    context = {
        'image':image
    }
    return render(request, 'image.html', context)
