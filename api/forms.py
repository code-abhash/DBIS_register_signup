# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    mobile_no = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'mobile_no']
