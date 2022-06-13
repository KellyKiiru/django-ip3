from .models import *
from django.forms import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)