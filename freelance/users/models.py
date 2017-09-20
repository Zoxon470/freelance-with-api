from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import F


class User(AbstractUser):
    CUSTOMER = 1
    EXECUTOR = 2

    USER_TYPES = (
        (CUSTOMER, 'Customer'),
        (EXECUTOR, 'Executor'),
    )

    user_type = models.IntegerField(choices=USER_TYPES, default=EXECUTOR, verbose_name='Тип пользователя')
    balance = models.DecimalField(decimal_places=2, max_digits=7, default=0, verbose_name='Баланс')

    def __str__(self):
        return self.username

    def update_balance(self, balance):
        User.objects.select_for_update().filter(user_type=User.CUSTOMER).update(
            balance=F('balance') - balance
        )
        User.objects.select_for_update().filter(user_type=User.EXECUTOR).update(
            balance=F('balance') + balance
        )