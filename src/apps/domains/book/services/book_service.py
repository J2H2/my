from apps.domains.book.models import Book
from apps.domains.book.repositories import BookRepository
from apps.domains.book.services.search_book_service import SearchBookService


class BookService:
    @classmethod
    def get_book_by_id(cls, book_id: int) -> Book:
        return BookRepository.get_by_id(book_id)

    @classmethod
    def get_book_by_isbn(cls, isbn: int) -> Book:
        try:
            return BookRepository.get_by_isbn(isbn=isbn)

        except Book.DoesNotExist:
            SearchBookService.find_books(str(isbn))
            return BookRepository.get_by_isbn(isbn=isbn)
