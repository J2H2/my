from django.db import models

from lib.base.models import BaseModel


class Book(BaseModel):
    isbn = models.BigIntegerField(unique=True, verbose_name='ISBN', )

    title = models.TextField(verbose_name='Title', )
    authors = models.TextField(verbose_name='authors', )
    publisher = models.TextField(verbose_name='publisher', )
    pub_date = models.DateField(verbose_name='publish date', )

    cover_l = models.TextField(verbose_name='Cover Large', )
    cover_s = models.TextField(verbose_name='Cover Small', )

    description = models.TextField(verbose_name='Description', )

    price = models.IntegerField(verbose_name='Price', )

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Book list'
