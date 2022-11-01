from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from passlib.hash import pbkdf2_sha256
from django.db.models.signals import post_save


# Create your models here.
class Usuario(models.Model):
   nControl = models.CharField(unique=True,max_length=9,primary_key = True)
   nombre=models.CharField(max_length=20)
   apellidoP=models.CharField(max_length=20)
   apellidoM=models.CharField(max_length=20)
   email=models.EmailField()
   semestre=models.IntegerField()
   password=models.CharField(max_length=256)
   def verificar_password(self,raw_password):
    return pbkdf2_sha256.verify(raw_password,self.password)
   def __str__(self) :
        return f'{self.nControl}'
   

class Profile(models.Model):
    user=models.OneToOneField(Usuario,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='Profile',null=True,blank=True)
    def __str__(self) :
        return f'Perfil de {self.user.nombre}'


class Post(models.Model):
    user=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='posts')
    fecha=models.DateTimeField(default=timezone.now)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='Post',null=True,blank=True)
    class Meta:
        ordering=['-fecha']
    def __str__(self) :
        return f'{self.user.nControl}: {self.contenido}'

def create_profile(sender,instance,created, **Kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile,sender=Usuario)