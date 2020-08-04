from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class ExtendedUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    socialLink = models.URLField(max_length=256)

    def __str__(self):
        return '{}'.format(self.user.name)

    class Meta:
        verbose_name = 'участника клуба'
        verbose_name_plural = 'участники клуба'


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    # img = models.ImageField() //TODO: Pillow required
    postText = models.TextField(verbose_name='Текст')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
