from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Picture, PictureForm

import random
#from .models import Image

def random_image_view(request):
    # Get all image IDs from the database
    image_ids = PictureForm.objects.values_list('id', flat=True)

    # Select a random image
    random_image = None
    if image_ids:
        random_id = random.choice(image_ids)
        random_image = PictureForm.objects.get(id=random_id)
    context = {
        'random_image': random_image
    }
    return render(request, 'random_image.html', context)

# Create your views here.
def index_view(request):
    if request.user.is_anonymous:
        return redirect(login_view)
        
    elif request.method == "POST":
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            picture = form.save(commit = False)
            picture.user = request.user
            picture.save()
            return redirect(index_view)
    else:
        #RANDOM IMAGE LOGIC
        image_ids = Picture.objects.values_list('id', flat=True).distinct()
        random_image = None
        if image_ids:
            random_id = random.choice(image_ids)
            random_image = Picture.objects.get(id=random_id)

        form = PictureForm()
        pictures = Picture.objects.all()
        return render(request ,'index.html',{'pictures': pictures, 'form':form,'random_image': random_image})

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
    form = PictureForm()
    pictures = Picture.objects.filter(user=request.user)
    List_objests=list(Picture.objects.filter(user=request.user))
    number=len(List_objests)
    return render(request ,'myprofile.html',{'pictures': pictures, 'form':form, 'number':number})
    


        
