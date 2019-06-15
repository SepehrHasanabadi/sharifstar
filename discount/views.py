from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic import FormView
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import forms
from accounts.models import User

class DiscountPerm(View):
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user) 
        if not user.has_perm('discount.can_view_discount'):
            return redirect(reverse_lazy('accounts:info', args=[user.user_type]))

        return super().dispatch(request, *args, **kwargs)

class UseDiscoutPerm(View):
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user) 
        if not user.has_perm('accounts.can_use_discount'):
            # return redirect(reverse_lazy('discount:index'))
            pass

        return super().dispatch(request, *args, **kwargs)

class Discount(LoginRequiredMixin, DiscountPerm, TemplateView):
    precent_form = forms.PrecentDiscountForm
    amount_form = forms.AmountDiscountForm
    template_name = 'discount/index.html'

    def post(self, request):
        post_data = request.POST or None
        precent_form = self.precent_form(post_data, prefix='precent')
        amount_form = self.amount_form(post_data, prefix='amount')

        context = self.get_context_data(precent_form=precent_form, amount_form=amount_form)

        if precent_form.is_valid():
            self.form_save(precent_form)
        if amount_form.is_valid():
            self.form_save(amount_form)

        return self.render_to_response(context)
    
    def form_save(self, form):
        obj = form.save(commit=False)
        obj.creator = User.objects.get(username=self.request.user) 
        obj.save()
        return obj

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class UseDiscount(LoginRequiredMixin, UseDiscoutPerm, TemplateView):
    precent_form = forms.PrecentUseDiscountForm
    amount_form = forms.AmountUseDiscountForm
    template_name = 'discount/use_discount.html'

    def post(self, request):
        post_data = request.POST or None
        precent_form = self.precent_form(post_data, prefix='precent', user=User.objects.get(username=self.request.user))
        amount_form = self.amount_form(post_data, prefix='amount')

        context = self.get_context_data(precent_form=precent_form, amount_form=amount_form)

        if precent_form.is_valid():
            self.form_save(precent_form)
        if amount_form.is_valid():
            self.form_save(amount_form)

        return self.render_to_response(context)
    
    def form_save(self, form):
        return form.save(commit=True)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)