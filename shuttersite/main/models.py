from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.


class Picture(models.Model):
    caption = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="/images")
    uploaded_on = models.DateTimeField(auto_now=True)


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ('caption', 'image')