from django.shortcuts import render ,redirect
from myawwards.models import *
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User


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

@login_required
def profile(request, username):
    title = f'@{profile.username}'
    profile = User.objects.get(username=username)
    posts = Post.get_profile_image(profile.id)
    
    if request.user == profile:
        return redirect('profile', username=request.user.username)
    context = {
        "profile": profile,
        "title":title,
        "posts":posts,
    }
    return render(request, 'profile.html', context)