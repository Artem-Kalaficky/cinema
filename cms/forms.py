from django.forms import ModelForm, modelformset_factory
from django import forms
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput, DateInput
from django.core.exceptions import ValidationError

from main.models import Film, Seo, Image


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {'image': FileInput(attrs={'type': 'file'})}


class SeoForm(ModelForm):
    class Meta:
        model = Seo
        fields = ('url', 'title', 'keyword', 'description')
        widgets = {'url': URLInput(attrs={'placeholder': 'URL',
                                          'size': 66}),
                   'title': TextInput(attrs={'placeholder': 'Title',
                                             'size': 66}),
                   'keyword': TextInput(attrs={'placeholder': 'Words',
                                               'size': 66}),
                   'description': Textarea(attrs={'rows': 3,
                                                  'cols': 68,
                                                  'placeholder': 'Description'})}


class DateInputWidget(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


# region FILM FORMS
class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('main_picture', 'trailer', 'type_2d', 'type_3d', 'type_imax', 'premier_date',
                  'description_ru', 'description_uk', 'name_ru', 'name_uk')
        widgets = {'name_ru': TextInput(attrs={'placeholder': 'Название фильма',
                                                'class': 'form-cont rol',
                                                'required': 'true'}),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                   'description_ru': Textarea(attrs={'rows': 4,
                                                     'cols': 100,
                                                     'placeholder': 'Текст описания',
                                                     'required': 'true'}),
                   'name_uk': TextInput(attrs={'placeholder': 'Назва фільму',
                                               'size': 30,
                                               'required': 'true'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'cols': 100,
                                                     'placeholder': 'Текст опису',
                                                     'required': 'true'}),
                   'trailer': URLInput(attrs={'placeholder': 'Ссылка на видео в youtube',
                                              'size': 90}),
                   'main_picture': FileInput(attrs={'type': 'file'}),
                   'premier_date': DateInputWidget(attrs={'type': 'date'})}



FilmGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# endregion FILM FORMS END


