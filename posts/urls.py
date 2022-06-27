from django.urls import path
from posts.views import *
from posts import views

urlpatterns = [
    path('nuevopost/', views.nuevopost, name="nuevopost"),
    path('tablapost/', views.tablapost, name="tablapost"),
    path('post/<int:id>', views.post, name="post"),
    path("deletepost/<int:id>", views.deletepost, name="deletepost"),
    path("editpost/<int:id>", views.editpost, name="editpost")
]