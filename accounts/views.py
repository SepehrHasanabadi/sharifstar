from django.shortcuts import render
from django.views.generic import FormView, View
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import forms as auth_forms
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from .models import User
from discount.models import Discount

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    authentication_form = auth_forms.AuthenticationForm

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=True)
        messages.success(
            request, 'You are signed up.')
        return redirect(reverse_lazy('accounts:info', args=[user.user_type]))

class Information(LoginRequiredMixin, FormView):
    template_name = 'accounts/info.html'

    def get_form_class(self):
        user_type = self.kwargs['user_type']
        if forms.StudentForm.match_code(user_type):
            return forms.StudentForm
        if forms.ParentForm.match_code(user_type):
            return forms.ParentForm
        if forms.SchoolForm.match_code(user_type):
            return forms.SchoolForm
        if forms.OperatorForm.match_code(user_type):
            return forms.OperatorForm

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        obj = form.save(commit=False)
        permission = Permission.objects.filter(codename='discount.can_view_discount').first()
        if not permission:
            content_type = ContentType.objects.get_for_model(Discount)
            permission = Permission.objects.create(
                codename='can_view_discount',
                name='can view discount',
                content_type=content_type,
            )
        user.user_permissions.add(permission)
        obj.user = user
        obj.save()
        return redirect(reverse_lazy('discount:index'))
