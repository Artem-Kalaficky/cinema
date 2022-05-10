from modeltranslation.translator import register, TranslationOptions
from main.models import Film


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('name', 'description')