from django.forms import ModelForm, modelformset_factory
from django import forms
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput, DateInput

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

# FILM FORMS------------------------------------------------------------------------------------------------------------
class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'description', 'main_picture', 'trailer', 'type_2d', 'type_3d', 'type_imax', 'premier_date')
        widgets = {'name':         TextInput(attrs={'placeholder': 'Название фильма',
                                                    'size': 30}),
                   'description':  Textarea(attrs={'rows': 4,
                                                   'cols': 100,
                                                   'placeholder': 'Текст'}),
                   'trailer':      URLInput(attrs={'placeholder': 'Ссылка на видео в youtube',
                                                   'size': 90}),
                   'main_picture': FileInput(attrs={'type': 'file'}),
                   'premier_date': DateInput(attrs={'placeholder': 'xx.xx.xxxx',
                                                    'type': 'date'})}


FilmGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# FILM FORMS END--------------------------------------------------------------------------------------------------------


