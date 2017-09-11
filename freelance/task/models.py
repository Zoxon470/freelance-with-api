from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание')
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0, verbose_name='Цена')
    assignee = models.ForeignKey('users.User', related_name='assignee', null=True, verbose_name='Исполнитель')
    created_by = models.ForeignKey('users.User', related_name='created_by', verbose_name='Кем был создан')

    def __str__(self):
        return self.title