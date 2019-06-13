from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect, reverse

from . import forms

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        request = self.request
        form.save(commit=True)
        messages.success(
            request, 'You are signed up. To activate the account, follow the link sent to the mail.')
        return redirect(reverse('accounts:signup'))