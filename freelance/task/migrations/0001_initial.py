# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Цена')),
            ],
        ),
    ]
