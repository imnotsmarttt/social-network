from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm

from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 'class': 'form-control', 'id': 'floatingInput'
        }),
        help_text=None
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 'class': 'form-control', 'id': 'floatingInput'
        }),
        strip=False,
        help_text=None,
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'city', 'country']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Логин',
            'email': 'Email',
            'city': 'Город',
            'country': 'Страна',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
        }


class UserLoginForm(AuthenticationForm):
    """User login form"""
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'id': 'floatingPassword'}),
    )

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(UserLoginForm, self).__init__(*args, **kwargs)


class UserUpdateCustomForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'city', 'country', 'phone', 'about_me', 'avatar']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Логин',
            'email': 'Email',
            'city': 'Город',
            'country': 'Страна',
            'about_me': 'Про себя',
            'phone': 'Номер телефона',
            'avatar': 'Фото профиля'
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
            'about_me': forms.Textarea(attrs={
                'class': 'form-control', 'id': 'floatingInput'
            }),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control', 'id': 'floatingInput'
        }),
    )

    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 'class': 'form-control', 'id': 'floatingInput'
        }),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Подтвердите новый пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password', 'class': 'form-control', 'id': 'floatingInput'
        }),
    )
