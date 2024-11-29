from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def index_view(request):
    if request.user.is_anonymous:
        return redirect(login_view)
    return render(request ,'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect(index_view)
        
        return render(request , "login.html", {'error':'Invalid Credentials'})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect(index_view)

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request,"signup.html",{'error':'Username already exists'})
        user = User.objects.create_user(username=username,password=password)
        user.save()
        return redirect(index_view)
    return render(request, "signup.html")

def about_view(request):
    if request.user.is_anonymous:
        return redirect(login_view)
    return render(request ,'about.html')


def myprofile_view(request):
    if request.user.is_anonymous:
        return redirect(login_view)
    return render(request ,'myprofile.html')
