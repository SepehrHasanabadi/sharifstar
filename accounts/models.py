from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as AuthUser
from django.core.validators import RegexValidator


STUDENT_CODE = "stu"
PARENT_CODE = "par"
SCHOOL_CODE = "sch"
OPERATOR_CODE = "opr"

class User(AuthUser):

    USER_TYPE = [
        (STUDENT_CODE, "Student"),
        (PARENT_CODE, "Parent"),
        (SCHOOL_CODE, "School"),
        (OPERATOR_CODE, "Operator"),
        ]
        
    user_type = models.CharField(
        _('user type'),
        blank=False,
        help_text=_('User\'s type of registration.'),
        choices=USER_TYPE,
        max_length=3,
    )

class NameModel(models.Model):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    class Meta:
        abstract = True 

class CustomerModel(NameModel):
    phone_number = models.CharField(_('phone number'), blank=True, max_length=16)
    birth_date = models.DateTimeField(_('birth date'))

class Student(CustomerModel):
    national_code = models.IntegerField(_('national code'))

    @staticmethod
    def get_code():
        return STUDENT_CODE

class Parent(CustomerModel):
    child_national_code = models.IntegerField(_('child national code'))

    @staticmethod
    def get_code():
        return PARENT_CODE

class School(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True)
    manager_name = models.CharField(_('manager name'), max_length=30, blank=True)
    phone_number = models.CharField(_('phone number'), blank=True, max_length=16)
    identity = models.IntegerField(
        _('phone number'),
        blank=True,
        unique=True,
        help_text=_('Required. Has to be unique'),
        error_messages={
            'unique': _('A school with that identity already exists.'),
        },
        validators=[
            RegexValidator(
                regex=r'^\d{8}$',
                message='must be a 8 digits text',
                code='invalid_identity'
            ),]
    )

    @staticmethod
    def get_code():
        return SCHOOL_CODE

class Operator(NameModel):
    OPERATOR_TYPE = [
        ("act", "accountancy"),
        ]
    operator_type = models.CharField(
        _('operator type'),
        blank=False,
        help_text=_('User\'s type of operator.'),
        choices=OPERATOR_TYPE,
        max_length=3,
    )

    @staticmethod
    def get_code():
        return OPERATOR_CODE

