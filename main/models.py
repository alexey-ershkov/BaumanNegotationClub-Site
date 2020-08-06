from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class ExtendedUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    socialLink = models.URLField(max_length=256)

    def __str__(self):
        return '{}'.format(self.user)

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


class Game(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название игры')
    date = models.DateTimeField(verbose_name='Дата и время игры', null=True)

    def __str__(self):
        return '{}'.format(self.title, self.date)

    class Meta:
        verbose_name = 'игра'
        verbose_name_plural = 'игры'


class GameRequest(models.Model):
    game = models.ForeignKey('Game', on_delete=models.DO_NOTHING, verbose_name='Игра', null=True)
    extUser = models.OneToOneField('ExtendedUser', on_delete=models.CASCADE, verbose_name='Участник')
    gameTimeWanted = models.TimeField(verbose_name='Предпочитаемое время', null=True)

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
