from modeltranslation.translator import register, TranslationOptions
from main.models import Film, Cinema, Hall, NewsOrProm, Page, Contact


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Cinema)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'condition')


@register(Hall)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(NewsOrProm)
class NewsOrPromTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('seo_text', 'name', 'description')



