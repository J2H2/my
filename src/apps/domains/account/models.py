from django.contrib.auth.models import UserManager
from django.db import models

from lib.base.models import BaseUserModel


class User(BaseUserModel):
    email = models.EmailField(max_length=254, unique=True, verbose_name='이메일', )

    is_active = models.BooleanField(default=True, verbose_name='계정 활성화 여부', )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = '계정'
        verbose_name_plural = '계정 리스트'
