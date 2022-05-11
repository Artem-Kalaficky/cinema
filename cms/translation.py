from modeltranslation.translator import register, TranslationOptions
from main.models import Film, Cinema, Hall


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Cinema)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'condition')

@register(Hall)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('description',)