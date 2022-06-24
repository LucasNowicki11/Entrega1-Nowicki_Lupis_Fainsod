from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to = "profile_image")
