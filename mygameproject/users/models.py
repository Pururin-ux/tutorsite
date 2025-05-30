# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # добавьте кастомные поля, если это необходимо
    username = models.DateField(blank=True, null=True)
    email = models.DateField(blank=True, null=True)
    password = models.DateField(blank=True, null=True)
    password2 = models.DateField(blank=True, null=True)
    # другие поля, которые вам нужны

    # Установите кастомные related_name для связей с группами и разрешениями
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # custom related_name для связи с группами
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # custom related_name для связи с разрешениями
        blank=True,
    )

    def __str__(self):
        return self.username
