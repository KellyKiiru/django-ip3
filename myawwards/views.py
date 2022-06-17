from multiprocessing import context
from django.shortcuts import render ,redirect, get_object_or_404
from myawwards.models import *
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *


# Create your views here.


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
def profile(request):
    #user_profile = get_object_or_404(User, username=username)
    #title = f'@{user_profile.username}'
    posts = Post.objects.all()
    context = {
        "profile": profile,
        #"title":title,
        "posts":posts,
    }
    if request.user == profile:
        return redirect('profile', context, username=request.user.username)

    return render(request, 'all-pages/profile.html', context)

def edit_profile(request,user_id):
    user=get_object_or_404(User,id=user_id)
    #user = User.objects.first()
    form=EditProfileForm()
    if request.method == 'POST':
        form=EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.user=user
            form.save()
            return redirect('profile')
        else:
            form=EditProfileForm()
    return render(request,'all-pages/edit_profile.html',{"form":form})


@login_required
def project(request, post_rated):
    post_rated = Post.objects.get(title=post_rated)
    ratings = Ratings.objects.filter( post_rated=post_rated).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save()
            rate.user = request.user
            rate.post_rated = post_rated
            rate.save()
            post_ratings = Ratings.objects.filter(post_rated=post_rated)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    context = {
        'post_rated': post_rated,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'all-pages/project.html', context)

@login_required
def newpost(request):
    current_user=request.user
    if request.method == 'POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
        return redirect('index')
    else:
        form=PostForm()
    return render(request, 'all-pages/new_post.html', {"form": form})

def search(request,):
    if request.method == "GET":
        title = request.GET.get('title',)
        search_results = Post.objects.filter(title__icontains=title).all()
        message = f'name'
        context =  {'title': title, 
        'search_results': search_results,
        'message': message}
        return render (request,'all-pages/search_results.html', context )
    else:
        message = "Please input title of project you want to post"
    
    return render (request, 'all-pages/search_results.html',context)

class Profilelist(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
