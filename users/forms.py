from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import TextInput, EmailInput, RadioSelect, Select, PasswordInput
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from cms.forms import DateInputWidget
from .models import UserProfile


class ChangeUserInfoForm(UserChangeForm):
    error_messages = {
        "password_mismatch": _("Введённые пароли не совпадают."),
    }

    password1 = forms.CharField(required=False, label=_('Пароль'), widget=PasswordInput(attrs={'class': 'form-control'}),
                                help_text=password_validation.password_validators_help_texts())
    password2 = forms.CharField(required=False, label=_('Повторить пароль'), widget=PasswordInput(attrs={'class': 'form-control'}),
                                help_text='Повторите пароль')

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'alias', 'email', 'address', 'card_number', 'is_ru', 'is_male',
                  'telephone', 'birth_date', 'city', 'password1', 'password2')
        widgets = {'first_name': TextInput(attrs={'class': 'form-control'}),
                   'last_name': TextInput(attrs={'class': 'form-control'}),
                   'alias': TextInput(attrs={'class': 'form-control'}),
                   'email': EmailInput(attrs={'class': 'form-control'}),
                   'address': TextInput(attrs={'class': 'form-control'}),
                   'card_number': TextInput(attrs={'class': 'form-control'}),
                   'is_ru': RadioSelect(choices=[(True, _('Русский')),
                                                 (False, _('Украинский'))]),
                   'is_male': RadioSelect(choices=[(True, _('Мужской')),
                                                   (False, _('Женский'))]),
                   'telephone': TextInput(attrs={'class': 'form-control'}),
                   'birth_date': DateInputWidget(attrs={'type': 'date',
                                                        'class': 'form-control'}),
                   'city': Select(attrs={'class': 'form-control'})}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 and not password2:
            pass
        else:
            if password1 and password2 and password1 != password2:
                raise ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
            return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password2")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password2", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        if not self.cleaned_data['password1']:
            user.is_active = True
            if commit:
                user.save()
            return user
        else:
            user.set_password(self.cleaned_data['password1'])
            user.is_active = True
            if commit:
                user.save()
            return user


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label=_('Пароль'), widget=PasswordInput(attrs={'class': 'form-control'}),
                                help_text=password_validation.password_validators_help_texts())
    password2 = forms.CharField(label=_('Повторить пароль'), widget=PasswordInput(attrs={'class': 'form-control'}),
                                help_text='Повторите пароль')

    class Meta:
        model = UserProfile
        fields = ('email', 'alias', 'last_name', 'first_name', 'is_male', 'password1', 'password2')
        widgets = {'first_name': TextInput(attrs={'class': 'form-control'}),
                   'last_name': TextInput(attrs={'class': 'form-control'}),
                   'alias': TextInput(attrs={'class': 'form-control'}),
                   'email': EmailInput(attrs={'class': 'form-control'}),
                   'is_male': RadioSelect(choices=[(True, _('Мужской')),
                                                   (False, _('Женский'))])}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(self.error_messages['password_mismatch'], code='password_mismatch')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        if commit:
            user.save()
        return user
