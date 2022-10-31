
import email
from django.shortcuts import redirect, render
from .models import Post,Usuario
from django.contrib.auth.models import User
from django.contrib import messages
from passlib.hash import pbkdf2_sha256

# Create your views here.
def  feed(request):
    posts=Post.objects.all()
    return render(request,'social/feed.html',{"posts":posts})

def register (request):
        if request.method == 'POST':
            nControl=request.POST['ncontrol']
            name=request.POST['nombre']
            first_name=request.POST['apellidoP']
            last_name=request.POST['apellidoM']
            semestre=request.POST['semestre']
            correo=request.POST['correo']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2'] 
            enc_password=pbkdf2_sha256.encrypt(pass1,rounds=12000,salt_size=32)

            if Usuario.objects.filter(nControl=nControl):
                messages.error(request,"Numero de control ya registrado")
                return redirect('register') 
            if Usuario.objects.filter(email=email):
                messages.error(request,"Correo institucional ya registrado")
            
            if pass1.__eq__(pass2):    
                Usuario.objects.create(
                nControl=nControl,
                nombre=name,
                apellidoP=first_name,
                apellidoM=last_name,
                semestre=semestre,
                email=correo,
                password=enc_password)    
                return redirect('login') 
                   
               
        return render(request,'social/register.html')
   
       
def  profile(request):
    return render(request,'social/profile.html')
def login(request):
    return render(request, 'social/acceso.html')
    