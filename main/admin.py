from django.contrib import admin

from main import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


class GameRequestAdmin(admin.ModelAdmin):
    list_display = ('extUser', 'gameTimeWanted', 'game')
    list_filter = ('game', 'extUser')


class RulesAdmin(admin.ModelAdmin):
    list_display = ('ruleTitle', 'position')


admin.site.register(models.ExtendedUser)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Game, GameAdmin)
admin.site.register(models.GameRequest, GameRequestAdmin)
admin.site.register(models.Rules, RulesAdmin)
