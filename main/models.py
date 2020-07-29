from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ExtendedUser:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    socialLink = models.CharField(max_length=128)
