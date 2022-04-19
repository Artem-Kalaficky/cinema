import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# class UserProfile(AbstractUser):
#     alies = models.CharField(max_length=30, verbose_name="Псевдоним")
#     address = models.CharField(max_length=128, verbose_name="Адрес")
#     card_number = models.IntegerField(verbose_name="Номер карты")
#     CHOICES = (
#         ('male', 'Мужской'),
#         ('female', 'Женский'),
#     )
#     gender = models.BooleanField(choices=CHOICES, default=True, verbose_name="")
#     telephone = models.CharField(max_length=20, verbose_name="")
#     birth_date = models.DateField(verbose_name="")
#     city = models.CharField(max_length=128, verbose_name="")
#     LANGUAGES = (
#         ('ru', 'Русский'),
#         ('uk', 'Украинский'),
#     )
#     language = models.BooleanField(choices=LANGUAGES, default=True, verbose_name="Язык")
