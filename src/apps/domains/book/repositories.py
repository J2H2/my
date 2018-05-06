from apps.domains.book.models import Book
from lib.base.repositories import BaseRepository


class BookRepository(BaseRepository):
    model_class = Book

    @classmethod
    def get_by_id(cls, book_id: int) -> Book:
        return Book.objects.get(id=book_id)

    @classmethod
    def get_by_isbn(cls, isbn: int) -> Book:
        return Book.objects.get(isbn=isbn)

    @classmethod
    def get_by_isbn(cls, isbn: int) -> Book:
        return Book.objects.get(isbn=isbn)
