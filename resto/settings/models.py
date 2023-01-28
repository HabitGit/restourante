from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return f'User {self.user}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'