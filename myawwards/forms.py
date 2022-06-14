from .models import *
from django.forms import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)
        
class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['post_rated', 'score']