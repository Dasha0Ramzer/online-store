from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", help_text="Введите свой Email")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон",
                             help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар",
                               help_text="Добавьте аватар")
    country = models.CharField(max_length=20, blank=True, null=True, verbose_name="Страна",
                               help_text="Введите страну проживания")
    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
