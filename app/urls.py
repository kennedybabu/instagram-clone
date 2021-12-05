from django.conf.urls import url
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.loginPage, name='login' ),
    path('logout/', views.logoutUser, name='logout' ),
    path('', views.home, name='home'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)