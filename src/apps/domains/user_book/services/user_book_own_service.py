from apps.domains.book.models import Book
from apps.domains.book.services.book_service import BookService
from apps.domains.user_book.models import UserBook


class UserBookOwnService:
    @classmethod
    def change_own_status(cls, user, book_id: int, own_status: int):
        book = BookService.get_book(book_id)
        cls._change_own_status(user, book, own_status)

    @classmethod
    def change_own_status_by_isbn(cls, user, isbn: int, own_status: int):
        book = BookService.get_book_by_isbn(isbn)
        cls._change_own_status(user, book, own_status)

    @classmethod
    def _change_own_status(cls, user, book: Book, own_status: int):
        user_book, _ = UserBook.objects.get_or_create(user=user, book=book)
        user_book.change_own_status(own_status)
        user_book.save()
