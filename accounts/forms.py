from django import forms
from django.contrib.auth import forms as auth_forms

from . import models


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.User
        fields = ['username', 'user_type', "password1", "password2"]
    
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.user_type = self.cleaned_data["user_type"]
        if commit:
            user.save()
        return user

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'

    @staticmethod
    def match_code(user_code):
        return user_code == models.Student.get_code()

class ParentForm(forms.ModelForm):
    class Meta:
        model = models.Parent
        fields = '__all__'

    @staticmethod
    def match_code(user_code):
        return user_code == models.Parent.get_code()

class SchoolForm(forms.ModelForm):
    class Meta:
        model = models.School
        fields = '__all__'

    @staticmethod
    def match_code(user_code):
        return user_code == models.School.get_code()

class OperatorForm(forms.ModelForm):
    class Meta:
        model = models.Operator
        fields = '__all__'

    @staticmethod
    def match_code(user_code):
        return user_code == models.Operator.get_code()
