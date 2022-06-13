from django.shortcuts import render
from myawwards.models import Post, Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    title =  "Myawwards"
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    context = {
        "posts": posts,
        "title":title,
        "profiles": profiles
    }
    return render(request,'all-pages/index.html',context)