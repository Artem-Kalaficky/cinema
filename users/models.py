from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .manager import CustomUserManager


CHOICES = (
    (None, _('Выберите город')),
    ('Одесса', _('Одесса')),
    ('Днепр', _('Днепр')),
    ('Чернигов', _('Чернигов')),
    ('Харьков', _('Харьков')),
    ('Житомир', _('Житомир')),
    ('Полтава', _('Полтава')),
    ('Херсон', _('Херсон')),
    ('Киев', _('Киев')),
    ('Запорожье', _('Запорожье')),
    ('Луганск', _('Луганск')),
    ('Донецк', _('Донецк')),
    ('Винница', _('Винница')),
    ('Кировоград', _('Кировоград')),
    ('Николаев', _('Николаев')),
    ('Суммы', _('Суммы')),
    ('Львов', _('Львов')),
    ('Черкасы', _('Черкасы')),
    ('Хмельницк', _('Хмельницк')),
    ('Волынь', _('Волынь')),
    ('Ровно', _('Ровно')),
    ('Ивано-Франковск', _('Ивано-Франковск')),
    ('Тернополь', _('Тернополь')),
    ('Закарпатье', _('Закарпатье')),
    ('Черновцы', _('Черновцы')),
)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('E-mail'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)
    first_name = models.CharField(max_length=150, blank=True, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=150, blank=True, verbose_name=_("Фамилия"))
    alias = models.CharField(max_length=30, blank=True, verbose_name=_("Псевдоним"))
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Адрес"))
    card_number = models.CharField(max_length=19, null=True, blank=True, verbose_name=_("Номер карты"))
    is_ru = models.BooleanField(default=True, verbose_name=_("Язык"))
    is_male = models.BooleanField(default=True, verbose_name=_("Пол"))
    telephone = models.CharField(max_length=20,  blank=True, verbose_name=_("Телефон"))
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("Дата рождения"))
    city = models.CharField(blank=True, max_length=20, choices=CHOICES, verbose_name=_("Город"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('Профиль')

    def __str__(self):
        return self.email

