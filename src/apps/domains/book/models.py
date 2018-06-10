from django.db import models

from apps.domains.book.constants import BookImageSourceType, BookImageType
from lib.base.models import BaseModel


def book_image_file_path(instance: 'BookImage', filename: str) -> str:
    return f'book/{instance.book_id % 1000}/{instance.book_id}/{filename}'


class BookImage(BaseModel):
    book_id = models.IntegerField(verbose_name='Book', )
    image_type = models.IntegerField(choices=BookImageType.get_choices(), verbose_name='Image type', )

    file = models.ImageField(upload_to=book_image_file_path, verbose_name='Image file', )

    source_type = models.IntegerField(choices=BookImageSourceType.get_choices(), verbose_name='Source type', )
    source_url = models.TextField(verbose_name='Cover Small', )

    class Meta:
        db_table = 'book_image'
        verbose_name = 'Book image'
        verbose_name_plural = 'Book imgae list'


class Book(BaseModel):
    isbn = models.BigIntegerField(unique=True, verbose_name='ISBN', )

    title = models.TextField(verbose_name='Title', )
    authors = models.TextField(verbose_name='authors', )
    publisher = models.TextField(verbose_name='publisher', )
    pub_date = models.DateField(verbose_name='publish date', )

    front_cover = models.ForeignKey(
        BookImage, on_delete=models.PROTECT, related_name='book_front_cover',
        null=True, blank=True, default=None, verbose_name='Front cover image',
    )
    spine = models.ForeignKey(
        BookImage, on_delete=models.PROTECT, related_name='book_spine',
        null=True, blank=True, default=None, verbose_name='Spine image',
    )
    back_cover = models.ForeignKey(
        BookImage, on_delete=models.PROTECT, related_name='book_back_cover',
        null=True, blank=True, default=None, verbose_name='Back cover image',
    )

    cover_url = models.TextField(null=True, blank=True, default=None, verbose_name='Cover Small', )
    save_cover = models.BooleanField(default=False, verbose_name='Cover file is saved', )

    description = models.TextField(null=True, blank=True, default=None, verbose_name='Description', )

    price = models.IntegerField(null=True, blank=True, default=None, verbose_name='Price', )

    class Meta:
        db_table = 'book'
        verbose_name = 'Book'
        verbose_name_plural = 'Book list'
