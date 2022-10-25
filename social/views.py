from django.shortcuts import render
from .models import Post

# Create your views here.
def  feed(request):
    posts=Post.objects.all()
    return render(request,'social/feed.html',{"posts":posts})

def  profile(request):
    return render(request,'social/profile.html')
    