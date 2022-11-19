

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Profile,Usuario,UserDetails
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import  authenticate,login



# Create your views here.

def  feed(request):
    posts=Post.objects.all()
    return render(request,'social/feed.html',{"posts":posts})

def register (request):
        if request.method == 'POST':
            nControl=request.POST['ncontrol']
            name=request.POST['nombre']
            apellidoP=request.POST['apellidoP']
            apellidoM=request.POST['apellidoM']
            semestre=request.POST['semestre']
            correo=request.POST['correo']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2'] 
            lastname=apellidoP+" "+apellidoM
        
            if User.objects.filter(username=nControl):
                messages.error(request,"Numero de control ya registrado")
                return redirect('register') 
            if Usuario.objects.filter(email=correo):
                messages.error(request,"Correo institucional ya registrado")   
           
            if pass1.__eq__(pass2):    
                  
                    myuser=User.objects.create_user(nControl,correo,pass1)
                    myuser.first_name=name
                    myuser.last_name=lastname 
                    myuser.save()
                    userDetails=UserDetails.objects.create(user=myuser,semestre=semestre)
                            
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


def signin(request):
    if request.method == 'POST':

            nControl=request.POST['ncontrol']
            pass1=request.POST['pass1']
            user=authenticate(username=nControl,password=pass1)
            if user is not None:
                login(request,user)
                posts=Post.objects.all()
                
                nControl=user.username
                if request.user.is_authenticated:
                  
                    return HttpResponseRedirect('/feed')    
                      
            else:
                messages.error(request,"Datos incorrectos")  
                return redirect('login')

                
                
                
         
    return render(request, 'social/acceso.html')
def post (request):
         if request.method == 'POST':
            user=get_object_or_404(User,pk=request.user.pk)
            contenido=request.POST['contenido']
            post=Post.objects.create(user=user,contenido=contenido)
            post.save()
            return HttpResponseRedirect('/feed')   
