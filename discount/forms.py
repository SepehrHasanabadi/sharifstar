from django import forms

from . import models

class PrecentDiscountForm(forms.ModelForm):
    class Meta:
        model = models.PercentDiscount
        fields = ['percent', 'count_expiration', 'start_date', 'end_date', 'used_date', 'code']

class AmountDiscountForm(forms.ModelForm):
    class Meta:
        model = models.AmountDiscount
        fields = ['amount', 'count_expiration', 'start_date', 'end_date', 'used_date', 'code']

    