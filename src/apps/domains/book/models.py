from django.db import models

from lib.base.models import BaseModel


class Book(BaseModel):
    isbn = models.BigIntegerField(unique=True, verbose_name='ISBN', )

    title = models.TextField(verbose_name='제목', )
    authors = models.TextField(verbose_name='작가들', )
    publisher = models.TextField(verbose_name='출판사', )
    pub_date = models.DateField(verbose_name='출판일', )

    cover_l = models.TextField(verbose_name='커버 Large', )
    cover_s = models.TextField(verbose_name='커버 Small', )

    description = models.TextField(verbose_name='설명', )

    price = models.IntegerField(verbose_name='가격', )

    class Meta:
        db_table = 'book'
        verbose_name = '책'
        verbose_name_plural = '첵 리스트'
