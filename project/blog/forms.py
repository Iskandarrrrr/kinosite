from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'content',
                  'photo',
                  'category',
                  'video')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название кино'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержимое кино'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'video': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на кино'
            })}


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, help_text="Максимум 16 символов !!!",
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователья'
                               }))

    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Пароль'
                               }))


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователья'
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше имя'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше фамилия'
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Почта'
    }))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
