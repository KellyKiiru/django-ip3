from .models import *
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)
        
class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['post_rated', 'score']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['design', 'usability', 'content']
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']