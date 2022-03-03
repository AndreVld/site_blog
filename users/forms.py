from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdvUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2',)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ('image', 'username', 'first_name', 'last_name', 'email', 'show_email', 'about_me',)
