from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    followers = ManyToManyField(User, related_name='followers')
