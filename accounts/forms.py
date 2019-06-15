from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from . import models
from discount.models import Discount

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
        fields = ['first_name', 'last_name', 'phone_number', 'birth_date', 'national_code']

    @staticmethod
    def match_code(user_code):
        return models.Student.match_code(user_code)
    
class ParentForm(forms.ModelForm):
    class Meta:
        model = models.Parent
        fields = ['first_name', 'last_name', 'phone_number', 'birth_date', 'child_national_code']

    @staticmethod
    def match_code(user_code):
        return models.Parent.match_code(user_code)

class SchoolForm(forms.ModelForm):
    class Meta:
        model = models.School
        fields = ['school_name', 'manager_name', 'phone_number', 'identity']

    @staticmethod
    def match_code(user_code):
        return models.School.match_code(user_code)

class OperatorForm(forms.ModelForm):
    class Meta:
        model = models.Operator
        fields = ['first_name', 'last_name', 'operator_type']

    @staticmethod
    def match_code(user_code):
        return models.Operator.match_code(user_code)
