from apps.domains.library.book.constants import OwnStatus, ReadStatus
from django.db import models
from django.utils import timezone

from apps.domains.account.models import User
from apps.domains.book.models import Book
from lib.base.models import BaseModel


class LibraryBook(BaseModel):
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT, related_name='user_1', verbose_name='User', )

    book = models.ForeignKey(Book, null=False, on_delete=models.PROTECT, related_name='user_book_1', verbose_name='Book', )

    own_status = models.IntegerField(choices=OwnStatus.get_choices(), default=OwnStatus.NONE, verbose_name='Own status', )
    own_date = models.DateTimeField(null=True, verbose_name='own date')

    read_status = models.IntegerField(choices=ReadStatus.get_choices(), default=ReadStatus.NONE, verbose_name='Read status', )
    read_date = models.DateTimeField(null=True, verbose_name='read date')

    class Meta:
        db_table = 'library_book'
        verbose_name = 'User book library'
        verbose_name_plural = 'User book library list'

    def change_own_status(self, own_status: int):
        self.own_status = own_status
        if self.own_status == OwnStatus.OWN:
            self.own_date = timezone.now()
        else:
            self.own_date = None

    def change_read_status(self, read_status: int):
        self.read_status = read_status
        if self.read_status == ReadStatus.READ:
            self.read_date = timezone.now()
        else:
            self.read_date = None
