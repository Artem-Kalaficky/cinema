from django.db import models
from django.contrib.auth.models import AbstractUser


# CHOICES = (
#     (None, 'Выберите город'),
#     ('1', 'Одесса'),
#     ('2', 'Днепр'),
#     ('3', 'Чернигов'),
#     ('4', 'Харьков'),
#     ('5', 'Житомир'),
#     ('6', 'Полтава'),
#     ('7', 'Херсон'),
#     ('8', 'Киев'),
#     ('9', 'Запорожье'),
#     ('10', 'Луганск'),
#     ('11', 'Донецк'),
#     ('12', 'Винница'),
#     ('13', 'Кировоград'),
#     ('14', 'Николаев'),
#     ('15', 'Суммы'),
#     ('16', 'Львов'),
#     ('17', 'Черкасы'),
#     ('18', 'Хмельницк'),
#     ('19', 'Волынь'),
#     ('20', 'Ровно'),
#     ('21', 'Ивано-Франковск'),
#     ('22', 'Тернополь'),
#     ('23', 'Закарпатье'),
#     ('24', 'Черновцы'),
# )
#
#
# class UserProfile(AbstractUser):
#     alias = models.CharField(max_length=30, verbose_name="Псевдоним")
#     address = models.CharField(max_length=128, verbose_name="Адрес")
#     card_number = models.IntegerField(verbose_name="Номер карты")
#     is_ru = models.BooleanField(default=True, verbose_name="Русский язык")
#     is_male = models.BooleanField(default=True, verbose_name="Мужской пол")
#     telephone = models.CharField(max_length=20, verbose_name="Телефон")
#     birth_date = models.DateField(verbose_name="Дата рождения")
#     city = models.CharField(max_length=2, choices=CHOICES, verbose_name="Город")

