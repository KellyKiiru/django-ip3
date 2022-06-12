from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(blank=True, upload_to='profile/')
    bio = models.TextField(default="My Bio", blank=True)
    name = models.CharField(max_length=60, blank=False)
    loaction = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    
    def save_profile(self):
        self.save()
    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    
    def __str__(self):
        return f'{self.user.username} - Profile'
     
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts")
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(blank=False, upload_to='posts/')
    description = models.TextField(max_length=255)
    technologies = models.CharField(max_length=300, blank=True)
    url = models.URLField(max_length=300, blank=True)
    date = models.DateField(auto_now_add=True,blank=True)
    
    def save_post(self):
        self.save()
        
    def __str__(self):
        return f'{self.title}'