from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index_view,name='home'),
    path("login",views.login_view,name='login' ),
    path("logout",views.logout_view,name='logout'),
    path("signup",views.signup_view,name="signup"),
    path("myprofile",views.myprofile_view,name="myprofile"),
    path("about",views.about_view,name="about"),
    #path("addimage", views.add_image_view, name="addimage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
        )
