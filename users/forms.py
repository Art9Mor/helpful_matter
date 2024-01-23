from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'full_name', 'photo', 'phone', 'town', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
