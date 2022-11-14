

from django.shortcuts import redirect, render
from .models import Post, Profile,Usuario

from django.contrib import messages
from django.contrib.auth import  authenticate
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
            if Usuario.objects.filter(email=correo):
                messages.error(request,"Correo institucional ya registrado")      
            if pass1.__eq__(pass2):    
                if Usuario.objects.filter(password=pass1):
                    messages.error(request,"Intente con otra contraseña") 
                else:
                
                 p1=Usuario(nControl=nControl,
                 nombre=name,
                 apellidoP=first_name,
                 apellidoM=last_name,
                 semestre=semestre,
                 email=correo,
                 password=pass1)
                 p1.save()
                 return redirect('login') 

            else:      
                messages.error(request,"Las contraseñas no coinciden")
                                        
        return render(request,'social/Registro.html')
   
       
def  profile(request,nControl):
    context={}
    usuario=Usuario.objects.get(nControl=nControl)
    profile=Profile.objects.get(user=usuario)

    context['nControl'] =usuario.nControl
    context['nombre'] = usuario.nombre
    context['apellidoP'] = usuario.apellidoP
    context['apellidoM'] = usuario.apellidoM
    context['email'] = usuario.email
    context['semestre'] = usuario.semestre
    context['imagen'] = profile.imagen.url
    


    return render(request,'social/profile.html',context)



def login(request):
    if request.method == 'POST':
            nControl=request.POST['ncontrol']
            pass1=request.POST['pass1']
            if Usuario.objects.filter(nControl=nControl) and Usuario.objects.filter(password=pass1):
                usuario=Usuario.objects.get(nControl=nControl)
                context={}               
                context['nControl'] =usuario.nControl
                return render(request,'social/layout.html')
            else:
                messages.error(request,"Datos incorrectos")  
                return redirect('login')

                
                
                
         
    return render(request, 'social/acceso.html')
    