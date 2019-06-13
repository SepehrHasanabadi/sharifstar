from django import forms
from django.contrib.auth import forms as auth_forms

from .models import User


class SignUpForm(auth_forms.UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'user_type', "password1", "password2"]
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.user_type = self.cleaned_data["user_type"]
        if commit:
            user.save()
        return user
