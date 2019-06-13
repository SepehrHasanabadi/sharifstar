from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


from . import forms

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = forms.SignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=True)
        messages.success(
            request, 'You are signed up.')
        return redirect(reverse_lazy('accounts:info', args=[user.user_type]))

class Information(FormView):
    template_name = 'accounts/info.html'
    success_url = 'discount:index'

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
