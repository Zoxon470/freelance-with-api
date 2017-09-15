from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CUSTOMER = 1
    EXECUTER = 2

    USER_TYPES = ((CUSTOMER, ('Customer')), (EXECUTER, ('Executer')),)

    user_type = models.IntegerField(choices=USER_TYPES, default=EXECUTER, verbose_name='Тип пользователя')
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0, verbose_name='Баланс')

    def __str__(self):
        return self.username