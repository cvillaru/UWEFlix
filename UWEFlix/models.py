from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

# class CustomUserCreationForm(UserCreationForm):
#     password1 = forms.CharField(
#         label = "Password",
#         strip = False,
#         widget = forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         help_text = validate_password.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label = "Password confirmation",
#         strip = False,
#         widget = forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
#         help_text = "Enter the same password as before, for verification",
#     )

#     class Meta:
#         model = User
#         fields 
