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
