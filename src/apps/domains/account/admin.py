from django.contrib import admin

from lib.base.admin import BaseModelAdmin
from .models import User


class UserAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('개인 정보', {'fields': ('email',)}),
        ('상태 정보', {'fields': ('is_active',)}),
        ('관련 날짜', {'fields': ('last_login', 'reg_date', 'update_date',)}),
    )


admin.site.register(User, UserAdmin)
