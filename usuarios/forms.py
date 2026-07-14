from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

from django.forms import ModelForm

from usuarios.models import UserProfile


class UserProfileForm(ModelForm):

    class Meta:

        model = UserProfile

        fields = (
            "telefono",
            "cargo",
            "avatar",
        )
