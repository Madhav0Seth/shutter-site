from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path("singedin",views.index,name='home' ),
    path("",views.login,name='login' ),
]
