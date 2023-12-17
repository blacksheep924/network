from django.contrib.auth.models import AbstractUser,User
from django.db import models


class User(AbstractUser):
    pass

class NewPost(models.Model):

    postContent = models.CharField(max_length=500)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "poster")
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):

    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "profile")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "follower")
    followed = models.BooleanField(default=False)


 
    

    

