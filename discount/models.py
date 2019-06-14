from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class Discount(models.Model):
    creator = models.ForeignKey('accounts.User', verbose_name=_('creator'), on_delete=models.CASCADE)
    count_expiration = models.IntegerField(_('count expiration'))
    create_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(_('start date'))
    end_date = models.DateTimeField(_('end date'))
    used_date = models.DateTimeField(_('used date'))
    code = models.CharField(
        _('code'),
        unique=True,
        max_length=5,
        help_text=_('Required. Has to be unique'),
        error_messages={
            'unique': _('A code already exists.'),
        },
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z1-9]{5}$',
                message='5 length is a must',
                code='invalid_code'
            ),]
    )

    class Meta:
        abstract = True

class PercentDiscount(Discount):
    percent = models.IntegerField(_('percent'))

class AmountDiscount(Discount):
    amount = models.IntegerField(_('amount'))