from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput

from main.models import Film, Seo



class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_picture', 'trailer', 'type_2d', 'type_3d', 'type_imax')
        widgets = {'name':         TextInput(attrs={'placeholder': 'Название фильма',
                                                    'size': 30}),
                   'description':  Textarea(attrs={'rows': 4,
                                                   'cols': 100,
                                                   'placeholder': 'Текст'}),
                   'trailer':      URLInput(attrs={'placeholder': 'Ссылка на видео в youtube',
                                                   'size': 90}),
                   'main_picture': FileInput(attrs={'type': 'file'}),}


class FilmSeoForm(ModelForm):
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
                                                  'placeholder': 'Description'}),}



