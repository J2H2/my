from django.contrib.auth.models import PermissionsMixin
from django.db import models

from lib.base.models import BaseUserModel
from .managers import UserManager


class User(PermissionsMixin, BaseUserModel):
    email = models.EmailField(max_length=254, unique=True, verbose_name='이메일', )

    is_active = models.BooleanField(default=True, verbose_name='계정 활성화 여부', )

    is_staff = models.BooleanField(default=False, verbose_name='관리자 여부', )
    is_superuser = models.BooleanField(default=False, verbose_name='최고관리자 여부', )

    last_login = models.DateTimeField(blank=True, null=True, editable=False, verbose_name='마지막 로그인')

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = '계정'
        verbose_name_plural = '계정 리스트'
