from django.contrib import admin

from lib.base.admin import BaseModelAdmin
from .models import User


class UserAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('User info', {'fields': ('email',)}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Related dates', {'fields': ('last_login', 'created', 'last_modified',)}),
    )
    readonly_fields = ('last_login', 'created', 'last_modified',)
    list_display = (
        'email', 'print_group', 'print_user_permissions', 'is_active', 'is_superuser', 'last_login',
    )
    list_filter = ('is_active', 'is_superuser',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    def print_group(self, obj) -> str:
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else 'There is no groups.'

    print_group.short_description = 'Group'

    def print_user_permissions(self, obj) -> str:
        return ','.join(
            [g.name for g in obj.user_permissions.all()]
        ) if obj.user_permissions.count() else 'There is no permissions.'

    print_user_permissions.short_description = 'Permissions'


admin.site.register(User, UserAdmin)
