from django import forms
from datetime import datetime
from django.db.models import Count

from . import models

class PrecentDiscountForm(forms.ModelForm):
    class Meta:
        model = models.PercentDiscount
        fields = ['percent', 'count_expiration', 'start_date', 'end_date', 'code']

class AmountDiscountForm(forms.ModelForm):
    class Meta:
        model = models.AmountDiscount
        fields = ['amount', 'count_expiration', 'start_date', 'end_date', 'code']

class PrecentUseDiscountForm(forms.Form):
    code = forms.CharField(label='Percent Discount Code')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PrecentUseDiscountForm, self).__init__(*args, **kwargs)

    def clean_code(self):
        try:
            code = self.code_text = self.cleaned_data["code"]
            discount = models.PercentDiscount.objects.get(code=code)
            if models.PercentDiscountLog.objects.filter(discount__code=code, user=self.user).exists():
                 raise forms.ValidationError('you used', code='you_used')   
            if models.PercentDiscount.objects.filter(start_date__lt=datetime.now(), end_date__gt=datetime.now()):
                raise forms.ValidationError('date expired', code='date_expired')
            if discount.count_expiration <= models.PercentDiscountLog.objects.filter(discount__code=code).count():
                raise forms.ValidationError('count expired', code='count_expired') 
        except models.PercentDiscount.DoesNotExist:
            raise forms.ValidationError('Not exists', code='not_exists')

    def save(self, commit=False):
        amount = models.PercentDiscountLog()
        amount.discount = models.PercentDiscount.objects.get(code=self.code_text)
        amount.user = self.user
        amount.save()

class AmountUseDiscountForm(forms.Form):
    code = forms.CharField(label='Amount Discount Code')

    def clean_code(self):
        try:
            discount = models.AmountDiscount.objects.get(code=self.code)
            if discount.start_date > datetime.now() or discount.end_date < datetime.now():
                raise forms.ValidationError('date expired', code='date_expired')
            if discount.count_expiration <= models.AmountDiscountLog.objects.filter(code=self.code).count():
                raise forms.ValidationError('count expired', code='count_expired') 
        except models.AmountDiscount.DoesNotExist:
            raise forms.ValidationError('Not exists', code='not_exists')

    def save(self, user, commit=False):
        amount = models.AmountDiscountLog()
        amount.discount = models.AmountDiscount.objects.get(code=self.code)
        amount.user = user
        amount.save()
        
