from django.contrib import admin

from apps.domains.book.models import Book
from lib.base.admin import BaseModelAdmin


class BookAdmin(BaseModelAdmin):
    fieldsets = (
        (None, {'fields': ('id', 'isbn',)}),
        ('Book info', {'fields': ('title', 'authors', 'publisher',)}),
        ('Covers', {'fields': ('cover_url', 'front_cover', 'spine', 'back_cover', )}),
        ('Price info', {'fields': ('price',)}),
        ('Related dates', {'fields': ('pub_date', 'created', 'last_modified',)}),
    )
    readonly_fields = ('id', 'created', 'last_modified',)
    list_display = (
        'isbn', 'title', 'authors', 'publisher', 'pub_date', 'created', 'last_modified',
    )
    search_fields = ('title', 'authors',)


admin.site.register(Book, BookAdmin)
