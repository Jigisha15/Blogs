from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    blogger = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.blogger