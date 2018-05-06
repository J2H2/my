from apps.domains.account.models import User
from apps.domains.book.services.book_service import BookService
from apps.domains.library.book.models import LibraryBook


class LibraryBookService:
    @classmethod
    def get_by_user_and_book_id(cls, user: User, book_id: int) -> LibraryBook:
        book = BookService.get_book_by_id(book_id)
        user_book, _ = LibraryBook.objects.get_or_create(user=user, book=book)
        return user_book

    @classmethod
    def get_by_user_and_isbn(cls, user: User, isbn: int) -> LibraryBook:
        book = BookService.get_book_by_isbn(isbn)
        library_book, _ = LibraryBook.objects.get_or_create(user=user, book=book)
        return library_book
