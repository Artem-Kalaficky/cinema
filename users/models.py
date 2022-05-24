from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .manager import CustomUserManager


CHOICES = (
    (None, 'Выберите город'),
    ('Одесса', 'Одесса'),
    ('Днепр', 'Днепр'),
    ('Чернигов', 'Чернигов'),
    ('Харьков', 'Харьков'),
    ('Житомир', 'Житомир'),
    ('Полтава', 'Полтава'),
    ('Херсон', 'Херсон'),
    ('Киев', 'Киев'),
    ('Запорожье', 'Запорожье'),
    ('Луганск', 'Луганск'),
    ('Донецк', 'Донецк'),
    ('Винница', 'Винница'),
    ('Кировоград', 'Кировоград'),
    ('Николаев', 'Николаев'),
    ('Суммы', 'Суммы'),
    ('Львов', 'Львов'),
    ('Черкасы', 'Черкасы'),
    ('Хмельницк', 'Хмельницк'),
    ('Волынь', 'Волынь'),
    ('Ровно', 'Ровно'),
    ('Ивано-Франковск', 'Ивано-Франковск'),
    ('Тернополь', 'Тернополь'),
    ('Закарпатье', 'Закарпатье'),
    ('Черновцы', 'Черновцы'),
)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    first_name = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Фамилия")
    alias = models.CharField(max_length=30, blank=True, verbose_name="Псевдоним")
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name="Адрес")
    card_number = models.CharField(max_length=19, null=True, blank=True, verbose_name="Номер карты")
    is_ru = models.BooleanField(default=True, verbose_name="Язык")
    is_male = models.BooleanField(default=True, verbose_name="Пол")
    telephone = models.CharField(max_length=20,  blank=True, verbose_name="Телефон")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    city = models.CharField(blank=True, max_length=20, choices=CHOICES, verbose_name="Город")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Профиль'

    def __str__(self):
        return self.email

