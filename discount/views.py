from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic import FormView
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import forms
from accounts.models import User
from . import models

class DiscountPerm(View):
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user) 
        if not user.has_perm('discount.can_view_discount'):
            return redirect(reverse_lazy('accounts:info', args=[user.user_type]))

        return super().dispatch(request, *args, **kwargs)

class UseDiscoutPerm(View):
    def dispatch(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user) 
        if not user.has_perm('discount.can_use_discount'):
            return redirect(reverse_lazy('discount:index'))

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

class DiscountViewItem:
    def __init__(self, code, date_generated, generator, used_count, remain_count, period_expiration):
        self.code = code
        self.date_generated = date_generated
        self.generator = generator
        self.used_count = used_count
        self.remain_count = remain_count
        self.period_expiration = period_expiration
    
class AdminReport(TemplateView):
    template_name = 'discount/list_discount.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['percent_discount'] = self.get_percent_discounts_items(models.PercentDiscount.objects.all()) 
        context['amount_discount'] = self.get_amount_discounts_items(models.AmountDiscount.objects.all())
        return context

    def get_percent_discounts_items(self, discounts):
        result = []
        for discount in discounts:
            remain_count = models.PercentDiscountLog.objects.filter(discount__code=discount.code).count()
            result.append(DiscountViewItem(discount.code, discount.create_at, discount.creator,\
                discount.count_expiration, remain_count, str(discount.start_date) + ' to ' + str(discount.end_date)))
        return result

    def get_amount_discounts_items(self, discounts):
        result = []
        for discount in discounts:
            remain_count = models.PercentDiscountLog.objects.filter(discount__code=discount.code).count()
            result.append(DiscountViewItem(discount.code, discount.create_at, discount.creator,\
                discount.count_expiration, remain_count, str(discount.start_date) + ' to ' + str(discount.end_date)))
        return result

class ListDiscount(TemplateView):
    template_name = 'discount/student_discount.html'

class ListPercentDiscount(ListDiscount):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = models.PercentDiscountLog.objects.filter(discount__code=kwargs['code']).values('user__username')
        return context
    
class ListAmountDiscount(ListDiscount):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = models.AmountDiscountLog.objects.filter(discount__code=kwargs['code']).values('user__username')
        return context