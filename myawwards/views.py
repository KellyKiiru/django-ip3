from django.shortcuts import render
# Create your views here.

def index(request):
    title =  "Myawwards"
    return render(request,'all-pages/index.html', {"title":title})