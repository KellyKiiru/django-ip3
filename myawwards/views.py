from django.shortcuts import render ,redirect, get_object_or_404
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
    user_profile = get_object_or_404(User, username=username)
    title = f'@{user_profile.username}'
    posts = Post.objects.all()
    context = {
        "profile": profile,
        "title":title,
        "posts":posts,
    }
    if request.user == profile:
        return redirect('profile', context, username=request.user.username)

    return render(request, 'profile.html', context)