from django.db import models


class AbstractDateTimeModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MoneyLog(AbstractDateTimeModel):
    user = models.ForeignKey('users.User')
    task = models.ForeignKey('task.Task', default=None, null=True)
    reason = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=7, decimal_places=2, default=0)


class TaskExpense(AbstractDateTimeModel):
    task = models.ForeignKey('task.Task')
    executor = models.ForeignKey('users.User')
    money = models.DecimalField(max_digits=7, decimal_places=2, default=0)
