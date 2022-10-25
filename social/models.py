
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='Profile',null=True,blank=True)
    def __str__(self) :
        return f'Perfil de {self.user.username}'


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    fecha=models.DateTimeField(default=timezone.now)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='Post',null=True,blank=True)
    class Meta:
        ordering=['-fecha']
    def __str__(self) :
        return f'{self.user.username}: {self.contenido}'