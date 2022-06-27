from django.urls import path
from posts.views import *
from users import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path("login", views.login, name="login"),
    ]