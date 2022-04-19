import datetime

from django.db import models

import users.models
#from users.models import UserProfile


class Image(models.Model):
    image = models.ImageField(verbose_name="Картинка")


class Seo(models.Model):
    url = models.URLField(verbose_name="URL")
    title = models.CharField(max_length=25, verbose_name="Title")
    keyword = models.CharField(max_length=30, verbose_name="Keywords")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = 'SEO блок'


class Cinema(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    condition = models.TextField(verbose_name="Условия")
    logo = models.ImageField(verbose_name="Логотип")
    top_banner = models.ImageField(verbose_name="Верхний баннер")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кинотеатры'
        verbose_name = 'Кинотеатр'


class Contact(models.Model):
    name = models.OneToOneField(Cinema, on_delete=models.PROTECT, verbose_name="Название")
    address = models.TextField(verbose_name="Адресс")
    coordinate = models.URLField(verbose_name="Координаты")
    logo = models.ImageField(verbose_name="Логотип")

    class Meta:
        verbose_name = 'Контакты'


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name="Кинотеатр")
    hall_number = models.IntegerField(verbose_name="Номер")
    description = models.TextField(verbose_name="Описание")
    scheme = models.ImageField(verbose_name="Схема")
    top_banner = models.ImageField(verbose_name="Верхний баннер")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")

    class Meta:
        verbose_name_plural = 'Залы'
        verbose_name = 'Зал'
        ordering = ['hall_number']
        unique_together = ['cinema', 'hall_number']


class Film(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    main_picture = models.ImageField(verbose_name="Главная картинка")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    trailer = models.URLField(verbose_name="Ссылка трейлера")
    TYPES = (
        (None, 'Выберите тип публикуемого фильма'),
        ('1', '2D'),
        ('2', '3D'),
        ('3', 'IMAX'),
    )
    type = models.CharField(max_length=1, choices=TYPES, default='1', verbose_name="Тип")
    premier_date = models.DateField(verbose_name="Дата премьеры")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['-premier_date']


class Session(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="Зал")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="Фильм")
    time = models.DateTimeField(verbose_name="Время")
    cost = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name_plural = 'Сеансы'
        verbose_name = 'Сеанс'
        ordering = ['time']
        unique_together = ['hall', 'film', 'time']


class Ticket(models.Model):
    pass


class NewsOrProm(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    main_picture = models.ImageField(verbose_name="Главная картинка")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    link_to_video = models.URLField(verbose_name="Видео-ссылка")
    pub_date = models.DateField(verbose_name="Дата публикации")
    status = models.BooleanField(default=True, verbose_name="Статус")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")
    type = models.BooleanField(verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']


class Page(models.Model):
    telephone1 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон 1")
    telephone2 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон 2")
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Контанкты")
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    main_picture = models.ImageField(null=True, blank=True, verbose_name="Главная картинка")
    images = models.ManyToManyField(Image, blank=True, verbose_name="Галерея картинок")
    date_created = models.DateField(verbose_name="Дата создания")
    status = models.BooleanField(default=True, verbose_name="Статус")
    is_main_page = models.BooleanField(default=False, verbose_name="Является главной")
    seo_text = models.TextField(null=True, blank=True, verbose_name="SEO текст")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'


class Slider(models.Model):
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    url = models.URLField(verbose_name="URL")
    text = models.TextField(null=True, blank=True, verbose_name="Текст")
    SPEEDS = (
        (None, 'Выберете скорость'),
        ('1', '5c'),
        ('2', '10c'),
        ('3', '15'),
    )
    speed = models.CharField(max_length=1, default='1', verbose_name="Скорость вращения")
    status = models.BooleanField(default=True, verbose_name="Статус")

    class Meta:
        verbose_name = 'Главный слайдер'


class Background(models.Model):
    pass


# class Email(models.Model):
#     letter = models.FileField(verbose_name="Письмо")
#     user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, verbose_name="Пользователь")
#
#     class Meta:
#         verbose_name = 'E-mail'










