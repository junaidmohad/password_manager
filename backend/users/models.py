from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'        #should not be a list
    REQUIRED_FIELDS = []

#no custom user manager?

class facts(models.Model):
    fact = models.CharField(max_length = 500)
