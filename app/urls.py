from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.registerUser, name='register' ),
    path('logout/', views.logoutUser, name='logout' ),
    path('login/', views.loginPage, name='login' ),
    path('like/<int:id>/', views.like_image, name='like_image'),

    path('', views.home, name='home'),
    path('image/(<int:id>/)', views.image, name='image'),
    path('search/', views.search_results, name='search_results'),
    path('new_image/', views.new_image, name='new_image'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)