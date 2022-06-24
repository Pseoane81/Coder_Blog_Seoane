from django.urls import path
from posts.views import *
from posts import views

urlpatterns = [
    path('nuevopost/', views.nuevopost, name="nuevopost"),
    
]