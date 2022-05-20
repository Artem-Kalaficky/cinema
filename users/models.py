from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .manager import CustomUserManager


CHOICES = (
    (None, 'Выберите город'),
    ('1', 'Одесса'),
    ('2', 'Днепр'),
    ('3', 'Чернигов'),
    ('4', 'Харьков'),
    ('5', 'Житомир'),
    ('6', 'Полтава'),
    ('7', 'Херсон'),
    ('8', 'Киев'),
    ('9', 'Запорожье'),
    ('10', 'Луганск'),
    ('11', 'Донецк'),
    ('12', 'Винница'),
    ('13', 'Кировоград'),
    ('14', 'Николаев'),
    ('15', 'Суммы'),
    ('16', 'Львов'),
    ('17', 'Черкасы'),
    ('18', 'Хмельницк'),
    ('19', 'Волынь'),
    ('20', 'Ровно'),
    ('21', 'Ивано-Франковск'),
    ('22', 'Тернополь'),
    ('23', 'Закарпатье'),
    ('24', 'Черновцы'),
)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Фамилия")
    alias = models.CharField(max_length=30, blank=True, verbose_name="Псевдоним")
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name="Адрес")
    card_number = models.CharField(max_length=19, null=True, blank=True, verbose_name="Номер карты")
    is_ru = models.BooleanField(default=True, verbose_name="Язык")
    is_male = models.BooleanField(default=True, verbose_name="Пол")
    telephone = models.CharField(max_length=20,  blank=True, verbose_name="Телефон")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    city = models.CharField(blank=True, max_length=2, choices=CHOICES, verbose_name="Город")

    def __str__(self):
        return self.email

