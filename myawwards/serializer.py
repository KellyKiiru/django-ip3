from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
     model=Profile
     fields=('profile_picture','bio','email')

class PostSerializer(serializers.ModelSerializer):
   class Meta:
     model=Post
     fields=('id','title', 'photo', 'description', 'url','profile','user')
