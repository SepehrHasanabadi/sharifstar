from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as AuthUser


class User(AuthUser):

    USER_TYPE = [
        ("stu", "Student"),
        ("par", "Parent"),
        ("sch", "School"),
        ("opr", "Operator"),
        ]
        
    user_type = models.CharField(
        _('user type'),
        blank=False,
        help_text=_('User\'s type of registration.'),
        choices=USER_TYPE,
        max_length=3,
    )


