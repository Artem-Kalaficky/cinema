from django.forms import ModelForm, modelformset_factory
from django import forms
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput, DateInput
from django.core.exceptions import ValidationError

from main.models import Film, Seo, Image, Cinema


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
                                          'class': 'form-control'}),
                   'title': TextInput(attrs={'placeholder': 'Title',
                                             'class': 'form-control'}),
                   'keyword': TextInput(attrs={'placeholder': 'Words',
                                               'class': 'form-control'}),
                   'description': Textarea(attrs={'rows': 3,
                                                  'class': 'form-control',
                                                  'placeholder': 'Description'})}


class DateInputWidget(forms.DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


# region FILM FORMS
class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_picture', 'trailer', 'type_2d', 'type_3d', 'type_imax', 'premier_date',
                  'description_uk', 'name_uk')
        widgets = {'name': TextInput(attrs={'placeholder': 'Название фильма',
                                            'class': 'form-control'}),
                   'description': Textarea(attrs={'rows': 4,
                                                  'class': 'form-control',
                                                  'placeholder': 'Текст описания'}),
                   'name_uk': TextInput(attrs={'placeholder': 'Назва фільму',
                                               'class': 'form-control',
                                               'required': 'true'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису',
                                                     'required': 'true'}),
                   'trailer': URLInput(attrs={'placeholder': 'Ссылка на видео в youtube',
                                              'class': 'form-control'}),
                   'main_picture': FileInput(attrs={'type': 'file'}),
                   'premier_date': DateInputWidget(attrs={'type': 'date'})}


FilmGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# endregion FILM FORMS END

# region FILM FORMS
class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = ('name', 'description', 'condition', 'logo', 'top_banner', 'name_uk', 'description_uk', 'condition_uk')
        widgets = {'name': TextInput(attrs={'placeholder': 'Название кинотеатра',
                                            'class': 'form-control'}),
                   'description': Textarea(attrs={'rows': 4,
                                                  'class': 'form-control',
                                                  'placeholder': 'Текст описания'}),
                   'condition': Textarea(attrs={'rows': 4,
                                                'class': 'form-control',
                                                'placeholder': 'Текст условий'}),
                   'name_uk': TextInput(attrs={'placeholder': 'Назва кінотеатру',
                                               'class': 'form-control',
                                               'required': 'true'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису',
                                                     'required': 'true'}),
                   'condition_uk': Textarea(attrs={'rows': 4,
                                                   'class': 'form-control',
                                                   'placeholder': 'Текст умов',
                                                   'required': 'true'}),
                   'logo': FileInput(attrs={'type': 'file'}),
                   'top_banner': FileInput(attrs={'type': 'file'})}


