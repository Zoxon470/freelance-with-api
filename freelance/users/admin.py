from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

admin.site.register(User, UserAdmin)
