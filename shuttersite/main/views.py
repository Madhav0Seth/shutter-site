from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect(login)
    return render(request ,'index.html')

def login(request):
    if request.method == "POST":
        return render(request , "login.html")
    return render(request, "login.html")