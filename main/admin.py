from django.contrib import admin

from main import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')


admin.site.register(models.ExtendedUser)
admin.site.register(models.Post, PostAdmin)
