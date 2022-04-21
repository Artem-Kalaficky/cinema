from django.forms import ModelForm
from django import forms

from main.models import Film


class FilmForm(ModelForm):
    name = forms.CharField(label='Название фильма', widget=forms.TextInput(attrs={'placeholder': 'Название фильма',
                                                                                  'size': 30}))
    description = forms.CharField(label='Описание', widget=forms.widgets.Textarea(attrs={'rows': 4,
                                                                       'cols': 100,
                                                                       'placeholder': 'Текст'}))
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_picture', 'trailer')