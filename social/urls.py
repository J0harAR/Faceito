from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



 
urlpatterns=[
    path('',views.feed, name='feed'),
    path('profile/<str:nControl>/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('acceso/',views.login, name='login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
