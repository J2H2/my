from apps.domains.book.models import Book
from apps.domains.book.services.book_service import BookService
from apps.domains.library.book.models import LibraryBook


class LibraryBookOwnService:
    @classmethod
    def change_own_status(cls, user, book_id: int, own_status: int):
        book = BookService.get_book_by_id(book_id)
        cls._change_own_status(user, book, own_status)

    @classmethod
    def change_own_status_by_isbn(cls, user, isbn: int, own_status: int):
        book = BookService.get_book_by_isbn(isbn)
        cls._change_own_status(user, book, own_status)

    @classmethod
    def _change_own_status(cls, user, book: Book, own_status: int):
        library_book, _ = LibraryBook.objects.get_or_create(user=user, book=book)
        library_book.change_own_status(own_status)
        library_book.save()
