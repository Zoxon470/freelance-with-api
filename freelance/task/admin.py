from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

admin.site.register(Task, TaskAdmin)

