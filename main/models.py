from django.db import models

from users.models import UserProfile


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Картинка")


class Seo(models.Model):
    url = models.URLField(verbose_name="URL")
    title = models.CharField(max_length=25, verbose_name="Title")
    keyword = models.CharField(max_length=30, verbose_name="Keywords")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = 'SEO блок'


class Cinema(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название кинотеатра")
    description = models.TextField(verbose_name="Описание")
    condition = models.TextField(verbose_name="Условия")
    logo = models.ImageField(upload_to='gallery/', verbose_name="Логотип")
    top_banner = models.ImageField(upload_to='gallery/', verbose_name="Фото верхнего баннера")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Кинотеатры'
        verbose_name = 'Кинотеатр'


class Contact(models.Model):
    status = models.BooleanField(default=True, verbose_name='Статус')
    name = models.CharField(max_length=30, verbose_name="Название кинотеатра")
    address = models.TextField(verbose_name="Адрес")
    coordinate = models.CharField(max_length=512, verbose_name="Координаты для карты")
    logo = models.ImageField(upload_to='gallery/', verbose_name="Лого")

    class Meta:
        verbose_name = 'Контакты'


class Hall(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, verbose_name="Кинотеатр")
    hall_number = models.IntegerField(verbose_name="Номер зала")
    description = models.TextField(verbose_name="Описание зала")
    scheme = models.ImageField(upload_to='gallery/', verbose_name="Схема зала")
    top_banner = models.ImageField(upload_to='gallery/', verbose_name="Верхний баннер")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    create_date = models.DateField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")
    is_base = models.BooleanField(default=False, verbose_name="Основной")

    class Meta:
        verbose_name_plural = 'Залы'
        verbose_name = 'Зал'
        ordering = ['hall_number']
        unique_together = ['cinema', 'hall_number']


class Film(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание")
    main_picture = models.ImageField(upload_to='gallery/', verbose_name="Главная картинка")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    trailer = models.CharField(max_length=128, verbose_name="Ссылка на трейлер")
    type_2d = models.BooleanField(default=True, verbose_name="2D")
    type_3d = models.BooleanField(default=False, verbose_name="3D")
    type_imax = models.BooleanField(default=False, verbose_name="IMax")
    premier_date = models.DateField(verbose_name="Дата премьеры")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['-premier_date']


class NewsOrProm(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    main_picture = models.ImageField(upload_to='gallery/', verbose_name="Главная картинка")
    images = models.ManyToManyField(Image, verbose_name="Галерея картинок")
    link_to_video = models.URLField(verbose_name="Ссылка на видео")
    pub_date = models.DateField(verbose_name="Дата публикации")
    status = models.BooleanField(default=True, verbose_name="Статус")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")
    type = models.BooleanField(verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']


class Page(models.Model):
    status = models.BooleanField(default=True, verbose_name="Статус")
    telephone1 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон 1")
    telephone2 = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон 2")
    seo_text = models.TextField(null=True, blank=True, verbose_name="SEO текст")
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Название")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    main_picture = models.ImageField(upload_to='gallery/', null=True, blank=True, verbose_name="Главная картинка")
    images = models.ManyToManyField(Image, blank=True, verbose_name="Галерея картинок")
    date_created = models.DateField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Контанкты")
    seo = models.OneToOneField(Seo, on_delete=models.PROTECT, verbose_name="SEO блок")
    is_base = models.BooleanField(default=False, verbose_name="Основная страница")
    is_main = models.BooleanField(default=False, verbose_name="Главная")
    is_contact = models.BooleanField(default=False, verbose_name="Контакты")

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'


class Carousel(models.Model):
    status = models.BooleanField(default=True, verbose_name='Статус')
    CHOICES = ((5000, '5с'),
               (10000, '10с'),
               (15000, '15с'))
    speed = models.IntegerField(choices=CHOICES, default=5000, verbose_name='Скорость')
    is_main = models.BooleanField(default=True, verbose_name='Главная верх')

    class Meta:
        verbose_name_plural = 'Карусели'
        verbose_name = 'Карусель'


class Slide(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Картинка")
    url = models.URLField(verbose_name="URL")
    text = models.CharField(max_length=45, null=True, blank=True, verbose_name="Текст")
    is_main = models.BooleanField(default=True, verbose_name='Главный слайд')

    class Meta:
        verbose_name_plural = 'Слайды'
        verbose_name = 'Слайд'


class Banner(models.Model):
    is_photo_bg = models.BooleanField(default=True, verbose_name='Фото на фоне')
    photo = models.ImageField(upload_to='gallery/', verbose_name="Фото")


class Session(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="Зал")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="Фильм")
    time = models.DateTimeField(verbose_name="Время")
    cost = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name_plural = 'Сеансы'
        verbose_name = 'Сеанс'
        ordering = ['time']
        unique_together = ['hall', 'film', 'time']


class Ticket(models.Model):
    sessions = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Сеанс")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Пользователь")
    place = models.CharField(max_length=2, verbose_name="Место")
    row = models.CharField(max_length=2, verbose_name="Ряд")
    status = models.BooleanField(default=False, verbose_name="Куплено?")

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class Mailing(models.Model):
    letter = models.FileField(upload_to="", null=True, blank=True, verbose_name="Письмо")

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'










