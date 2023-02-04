from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput

from settings.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birthday')

        widgets = {
            'birthday': DateInput()
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')