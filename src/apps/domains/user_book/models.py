from datetime import datetime

from django.db import models
from django.utils import timezone

from apps.domains.account.models import User
from apps.domains.book.models import Book
from apps.domains.user_book.constants import OwnStatus, ReadStatus
from lib.base.models import BaseModel


class UserBook(BaseModel):
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT, related_name='user_1', verbose_name='유저', )

    book = models.ForeignKey(Book, null=False, on_delete=models.PROTECT, related_name='user_book_1', verbose_name='책', )

    own_status = models.IntegerField(choices=OwnStatus.get_choices(), default=OwnStatus.NONE, verbose_name='소유 상태', )
    own_date = models.DateTimeField(null=True, verbose_name='구매일')

    read_status = models.IntegerField(choices=ReadStatus.get_choices(), default=ReadStatus.NONE, verbose_name='읽기 상태', )
    read_date = models.DateTimeField(null=True, verbose_name='읽은 날')

    class Meta:
        db_table = 'user_book'
        verbose_name = '유저 책'
        verbose_name_plural = '유저 첵 리스트'

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
