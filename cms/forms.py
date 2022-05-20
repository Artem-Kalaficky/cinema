from django.forms import ModelForm, modelformset_factory
from django import forms
from django.forms.widgets import TextInput, Textarea, URLInput, FileInput, NumberInput, RadioSelect

from main.models import Film, Seo, Image, Cinema, Hall, NewsOrProm, Page, Contact, Carousel, Slide, Banner


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


# region FILM forms
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
                                               'class': 'form-control'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису'}),
                   'trailer': URLInput(attrs={'placeholder': 'Ссылка на видео в youtube',
                                              'class': 'form-control'}),
                   'main_picture': FileInput(attrs={'type': 'file'}),
                   'premier_date': DateInputWidget(attrs={'type': 'date'})}


FilmGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# endregion FILM forms

# region CINEMA forms
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
                                               'class': 'form-control'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису'}),
                   'condition_uk': Textarea(attrs={'rows': 4,
                                                   'class': 'form-control',
                                                   'placeholder': 'Текст умов'}),
                   'logo': FileInput(attrs={'type': 'file'}),
                   'top_banner': FileInput(attrs={'type': 'file'})}


CinemaGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# endregion CINEMA forms

# region HALL forms
class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = ('hall_number', 'description', 'scheme', 'top_banner', 'description_uk', 'is_base')
        widgets = {'hall_number': NumberInput(attrs={'placeholder': '№',
                                                     'class': 'form-control'}),
                   'description': Textarea(attrs={'rows': 4,
                                                  'class': 'form-control',
                                                  'placeholder': 'Текст описания'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису'}),
                   'scheme': FileInput(attrs={'type': 'file'}),
                   'top_banner': FileInput(attrs={'type': 'file'})}


HallGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# endregion HALL forms

# region NEWS forms
class NPForm(ModelForm):
    class Meta:
        model = NewsOrProm
        fields = ('name', 'description', 'main_picture', 'link_to_video', 'status', 'pub_date', 'name_uk',
                  'description_uk', 'type')
        widgets = {'name': TextInput(attrs={'placeholder': 'Название',
                                            'class': 'form-control'}),
                   'description': Textarea(attrs={'rows': 4,
                                                  'class': 'form-control',
                                                  'placeholder': 'Текст описания'}),
                   'name_uk': TextInput(attrs={'placeholder': 'Назва',
                                               'class': 'form-control'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису'}),
                   'main_picture': FileInput(attrs={'type': 'file'}),
                   'link_to_video': URLInput(attrs={'placeholder': 'Ссылка на видео в youtube',
                                                    'class': 'form-control'}),
                   'pub_date': DateInputWidget(attrs={'type': 'date'})}


NPGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
# endregion NEWS forms

# region PAGE forms
class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ('status', 'telephone1', 'telephone2', 'seo_text', 'seo_text_uk', 'name', 'name_uk', 'description',
                  'description_uk', 'main_picture', 'is_base', 'is_main', 'is_contact')
        widgets = {'telephone1': TextInput(attrs={'placeholder': '777-77-77',
                                                  'class': 'form-control'}),
                   'telephone2': TextInput(attrs={'placeholder': '777-77-77',
                                                  'class': 'form-control'}),
                   'seo_text': Textarea(attrs={'rows': 4,
                                               'class': 'form-control',
                                               'placeholder': 'SEO-текст'}),
                   'seo_text_uk': Textarea(attrs={'rows': 4,
                                                  'class': 'form-control',
                                                  'placeholder': 'SEO-текст',
                                                  'required': 'true'}),
                   'name': TextInput(attrs={'placeholder': 'Название страницы',
                                            'class': 'form-control'}),
                   'description': Textarea(attrs={'rows': 4,
                                                  'class': 'form-control',
                                                  'placeholder': 'Текст описания'}),
                   'name_uk': TextInput(attrs={'placeholder': 'Назва сторінки',
                                               'class': 'form-control'}),
                   'description_uk': Textarea(attrs={'rows': 4,
                                                     'class': 'form-control',
                                                     'placeholder': 'Текст опису'}),
                   'main_picture': FileInput(attrs={'type': 'file'})}


PageGalleryFormSet = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'address', 'coordinate', 'logo', 'status')
        widgets = {'name': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Название кинотеатра'}),
                   'address': Textarea(attrs={'rows': 4,
                                              'class': 'form-control',
                                              'placeholder': 'Введите адрес кинотеатра'}),
                   'coordinate': TextInput(attrs={'placeholder': 'Координаты для карты',
                                                  'class': 'form-control'}),
                   'logo': FileInput(attrs={'type': 'file'})}


ContactFormSet = modelformset_factory(Contact, form=ContactForm, extra=0, can_delete=True)
# endregion PAGE forms

# region BANNERS forms
class CarouselForm(ModelForm):
    class Meta:
        model = Carousel
        fields = ('status', 'speed', 'is_main')


class SlideForm(ModelForm):
    class Meta:
        model = Slide
        fields = ('image', 'url', 'text', 'is_main')
        widgets = {'image': FileInput(attrs={'type': 'file'}),
                   'url': URLInput(attrs={'placeholder': 'URL',
                                          'class': 'form-control'}),
                   'text': TextInput(attrs={'placeholder': 'Текст',
                                            'class': 'form-control'})}


SlideFormSet = modelformset_factory(Slide, form=SlideForm, extra=0, can_delete=True)

class BannerForm(ModelForm):
    class Meta:
        model = Banner
        fields = ('is_photo_bg', 'photo')
        widgets = {'photo': FileInput(attrs={'type': 'file'}),
                   'is_photo_bg': RadioSelect(choices=[(True, 'Фото на фоне'),
                                                       (False, 'Просто фон')])}
# endregion BANNERS forms




