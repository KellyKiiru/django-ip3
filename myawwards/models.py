from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.PictureField(blank=True, upload_to='profile/')
    bio = models.TextField(default="My Bio", blank=True)
    name = models.CharField(max_length=60, blank=False)
    loaction = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    
    def save_profile(self):
        self.save()
    
    def __str__(self):
        return f'{self.user.username} - Profile'
     