from django.contrib import admin

from apps.domains.book.models import Book
from lib.base.admin import BaseModelAdmin


class BookAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'isbn',)}),
        ('정보', {'fields': ('title', 'authors', 'publisher',)}),
        ('가격 정보', {'fields': ('price',)}),
        ('관련 날짜', {'fields': ('pub_date', 'created', 'last_modified',)}),
    )
    readonly_fields = ('id', 'created', 'last_modified',)
    list_display = (
        'isbn', 'title', 'authors', 'publisher', 'pub_date', 'created', 'last_modified',
    )
    search_fields = ('title', 'authors',)


admin.site.register(Book, BookAdmin)
