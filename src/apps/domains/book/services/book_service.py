from apps.domains.book.models import Book
from apps.domains.book.services.search_book_service import SearchBookService


class BookService:
    @classmethod
    def get_book(cls, book_id: int) -> Book:
        return Book.objects.get(id=book_id)

    @classmethod
    def get_book_by_isbn(cls, isbn: int) -> Book:
        try:
            return Book.objects.get(isbn=isbn)

        except Book.DoesNotExist:
            SearchBookService.find_books(str(isbn))
            return Book.objects.get(isbn=isbn)
