from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
import re


# Create your models here.


class ExtendedUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/', null=True, verbose_name='Аватар пользователя',
                               default='users/default-avatar.png')
    socialLink = models.URLField(max_length=256)

    def __str__(self):
        return '{}'.format(self.user.first_name + ' ' + self.user.last_name)

    class Meta:
        verbose_name = 'участника клуба'
        verbose_name_plural = 'участники клуба'


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    postText = models.TextField(verbose_name='Текст')
    img = models.ImageField(upload_to='posts/', null=True, verbose_name='Изображение', blank=True)
    youtubeVideo = models.URLField(
        verbose_name='Видео на youtube (ссылка в виде https://youtube.com/embed/<код видео>, где код видео идет после'
                     ' watch?v= в оригинальной ссылке)',
        null=True, blank=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Game(models.Model):
    types = (('K', 'Классика'), ('C', 'Ситуационная'))
    title = models.CharField(max_length=128, verbose_name='Название игры')
    gameType = models.CharField(choices=types, verbose_name='Тип игры', max_length=1, default='K')
    date = models.DateTimeField(verbose_name='Дата и время игры', null=True)
    comments = models.TextField(verbose_name='Комментарии к игре (видно только администратору)', blank=True)
    have_my_request = models.BooleanField(verbose_name='Доп поле для отрисовки данных на странице игр', default=False)

    def __str__(self):
        return '{}'.format(self.title, self.date)

    class Meta:
        verbose_name = 'игра'
        verbose_name_plural = 'игры'


class GameRequest(models.Model):
    status = (('N', 'Новая заявка'), ('W', 'Ожидает подверждения'), ('С', 'Заявка подтверждена'))
    requestStatus = models.CharField(choices=status, verbose_name='Статус заявки', max_length=1, default='N')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name='Игра', null=True)
    extUser = models.ForeignKey('ExtendedUser', on_delete=models.CASCADE, verbose_name='Участник', null=True)
    social = models.CharField(verbose_name='ссылка на профиль в соц сети', max_length=256)
    messageToUser = models.TextField(verbose_name='Сообщение для пользователя', blank=True, null=True)
    tableLink = models.URLField(verbose_name='Ссылка на турнирную таблицу игры', blank=True, null=True)
    gameLink = models.URLField(verbose_name='Ссылка на игру (например, если игра в Zoom)', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.extUser.user, self.game.title)

    class Meta:
        verbose_name = 'запрос на игру'
        verbose_name_plural = 'запросы на игру'


class Rules(models.Model):
    ruleTitle = models.CharField(max_length=128, verbose_name='Название пункта правил')
    ruleText = models.TextField(verbose_name='Правила')
    position = models.PositiveSmallIntegerField(unique=True, verbose_name='Номер по порядку')

    def __str__(self):
        return '{}'.format(self.ruleTitle, self.position)

    class Meta:
        verbose_name = 'правило'
        verbose_name_plural = 'правила'
