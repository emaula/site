from django import forms

from django.contrib.auth.models import User
from .models import Professor


class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class ProfessorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('picture', )
