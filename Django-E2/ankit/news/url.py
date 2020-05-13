from django.contrib import admin
from django.urls import path
from . import views
#. is same folder


urlpatterns = [
    path('',views.home,name='news-home'),
    path('about/',views.about,name='news-about'),
  
    
    
]