from django.contrib import admin
from django.urls import path
from .views import home, my_logout, cadastrar_usuario

urlpatterns = [
    path('', home, name="home"),
    path('logout', my_logout, name="logout"),
    path('cadastrar', cadastrar_usuario, name="cadastrar"),

]