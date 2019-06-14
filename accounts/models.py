from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as AuthUser, Group
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)

    class Meta:
        abstract = True 

class CustomerModel(NameModel):
    phone_number = models.CharField(_('phone number'), max_length=16, blank=False)
    birth_date = models.DateTimeField(_('birth date'), blank=False)

class Student(CustomerModel):
    national_code = models.IntegerField(_('national code'), blank=False)

    class Meta:
        permissions = [('student_discount', 'Student discount')]

    @staticmethod
    def get_code():
        return STUDENT_CODE

class Parent(CustomerModel):
    child_national_code = models.IntegerField(_('child national code'), blank=False)

    @staticmethod
    def get_code():
        return PARENT_CODE

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    school_name = models.CharField(_('school name'), max_length=30, blank=False)
    manager_name = models.CharField(_('manager name'), max_length=30, blank=False)
    phone_number = models.CharField(_('phone number'), blank=False, max_length=16)
    identity = models.IntegerField(
        _('Identity'),
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

