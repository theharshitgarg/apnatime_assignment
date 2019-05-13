from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm

from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30,
                                required=False,
                                help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    date_of_birth = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"),
        help_text='Format mm/dd/YYYY')
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'address', 'preferred_language',
                  'date_of_birth', 'avatar')


# class SignUpForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = [
# 			'username', 'password',  'email', 'first_name', 'last_name', 'date_of_birth',
# 			'address', 'preferred_language'
# 		]
