from django import forms
from django.forms.widgets import TextInput, EmailInput, RadioSelect, Select

from cms.forms import DateInputWidget
from .models import UserProfile


class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'alias', 'email', 'address', 'card_number', 'is_ru', 'is_male',
                  'telephone', 'birth_date', 'city')
        widgets = {'first_name': TextInput(attrs={'class': 'form-control'}),
                   'last_name': TextInput(attrs={'class': 'form-control'}),
                   'alias': TextInput(attrs={'class': 'form-control'}),
                   'email': EmailInput(attrs={'class': 'form-control'}),
                   'address': TextInput(attrs={'class': 'form-control'}),
                   'card_number': TextInput(attrs={'class': 'form-control'}),
                   'is_ru': RadioSelect(choices=[(True, 'Русский'),
                                                 (False, 'Украинский')]),
                   'is_male': RadioSelect(choices=[(True, 'Мужской'),
                                                   (False, 'Женский')]),
                   'telephone': TextInput(attrs={'class': 'form-control'}),
                   'birth_date': DateInputWidget(attrs={'type': 'date',
                                                        'class': 'form-control'}),
                   'city': Select(attrs={'class': 'form-control'})}
