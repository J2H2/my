from apps.domains.book.models import Book
from apps.domains.book.services.book_service import BookService
from apps.domains.library.book.models import LibraryBook


class LibraryBookReadService:
    @classmethod
    def change_read_status(cls, user, book_id: int, read_status: int):
        book = BookService.get_book(book_id)
        cls._change_read_status(user, book, read_status)

    @classmethod
    def change_read_status_by_isbn(cls, user, isbn: int, read_status: int):
        book = BookService.get_book_by_isbn(isbn)
        cls._change_read_status(user, book, read_status)

    @classmethod
    def _change_read_status(cls, user, book: Book, read_status: int):
        user_book, _ = LibraryBook.objects.get_or_create(user=user, book=book)
        user_book.change_read_status(read_status)
        user_book.save()
