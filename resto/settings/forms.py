from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput


class ProfileSettingsForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control'
            })
        }