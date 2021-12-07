from django.conf.urls import url
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.registerUser, name='register' ),
    path('logout/', views.logoutUser, name='logout' ),
    path('login/', views.loginPage, name='login' ),
    path('<int:pk>/', views.like_post, name="like_post"),

    path('', views.home, name='home'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^search/', views.search_results, name='search_results'),
    path('new_image/', views.new_image, name='new_image'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)