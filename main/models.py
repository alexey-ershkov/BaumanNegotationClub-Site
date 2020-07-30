from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class ExtendedUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    socialLink = models.URLField(max_length=256)

    def __str__(self):
        return '{}'.format(self.user.name)

    class Meta:
        verbose_name = 'Участника клуба'
        verbose_name_plural = 'Участники клуба'

