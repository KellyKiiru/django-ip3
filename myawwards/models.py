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
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
    
    @classmethod
    def all_posts(cls):
        return cls.objects.all()
    
    
    @classmethod
    def get_profile_image(cls, profile):
        posts = Post.objects.filter(user__pk=profile)
        return posts
        
    def __str__(self):
        return f'{self.title}'


class Ratings(models.Model):
    INPUT = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design=models.IntegerField(choices=INPUT, default=0, blank=True)
    usability=models.IntegerField(choices=INPUT, blank=True)
    content=models.IntegerField(choices=INPUT, blank=True)
    score=models.IntegerField(default=0, blank=True)
    post_rated = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='ratings',null=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Ratings.objects.filter(post_id=id).all()
        return ratings
    
    def __str__(self):
        return f'{self.post_rated} Rating'