from email import message
from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm,
from django.contrib import message

# Create your views here.
def  feed(request):
    posts=Post.objects.all()
    return render(request,'social/feed.html',{"posts":posts})

def register (request):
        if request.method == 'POST':
            form =UserCreationForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']

                message.success(request,f'Usuario {username} creado')
        else:
             form =UserCreationForm()
        return render(request,'social/register.html',{"form":form})

def  profile(request):
    return render(request,'social/profile.html')
    