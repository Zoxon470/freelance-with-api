from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2

    USER_TYPES = ((CUSTOMER, 'CUSTOMER'), (EXECUTOR, 'EXECUTOR'))

    name = models.CharField(blank=True, max_length=255, verbose_name='Имя пользователя')
    user_type = models.CharField(choices=USER_TYPES, default=EXECUTOR, max_length=255, verbose_name='Тип пользователя')
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0, verbose_name='Баланс')

    def __str__(self):
        return self.username