from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Comment, Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginPage(request):
    context = {

    }

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = Profile.objects.get(username = username)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
        
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    form = UserCreationForm()
    context = {
        'form':form
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error occurred during registration')
   
    return render(request, 'registration.html', context)

@login_required(login_url='login')
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
    comments = image.comment_set.all()

    if request.method == 'POST':
        comment = Comment.objects.create (
            user = request.user,
            image = image,
            comment_content = request.POST.get('comment_content')
        )

        return redirect('home')
    context = {
        'image':image,
        'comments': comments
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
