from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Profile

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


def search_results(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_query = request.GET.get('profile')
        searched_profiles = Profile.search_profile(search_query)
        print(searched_profiles)
        message = f'{search_query}'
        context = {
           'message':message,
           'searched_profiles':searched_profiles
        }

        return render (request, 'search.html', context)
    else:
        message = 'You havent searched for any profile'
        return render(request, 'search.html', {'message':message})
