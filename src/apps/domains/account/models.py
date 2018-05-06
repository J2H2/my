from django.contrib.auth.models import PermissionsMixin
from django.db import models

from lib.base.models import BaseUserModel
from .managers import UserManager


class User(PermissionsMixin, BaseUserModel):
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email', )

    is_active = models.BooleanField(default=True, verbose_name='Active user', )

    is_staff = models.BooleanField(default=False, verbose_name='Staff', )
    is_superuser = models.BooleanField(default=False, verbose_name='Super staff', )

    last_login = models.DateTimeField(blank=True, null=True, editable=False, verbose_name='last login date')

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
