from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    followers = ManyToManyField(User, related_name='followers', blank=True)
    profile_photo = models.ImageField('image', blank=True, null=True)

    def save_profile(self):
        '''
        save profile
        '''
        self.save()

    def delete_profile(self):
        '''
        delete profile
        '''
        self.delete()

    def update_profile(self, new):
        '''
        method that will update the profile
        '''
        self.username = new.username
        self.bio = new.bio
        self.profile_photo = new.profile_photo
        self.save()

    def total_followers(self):
        '''
        method that will return the total no of followers
        '''
        return self.followers.count()

    @classmethod
    def search_profile(cls, search_query):
        profile = cls.objects.filter(username__icontains = search_query)
        return profile

    def __str__(self):
        return self.username
