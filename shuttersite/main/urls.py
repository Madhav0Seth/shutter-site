from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path("",views.index_view,name='home'),
    path("login",views.login_view,name='login' ),
    path("logout",views.logout_view,name='logout'),
    path("signup",views.signup_view,name="signup"),
]
