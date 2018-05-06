from typing import List

from apps.domains.account.models import User
from apps.domains.library.book.models import LibraryBook
from lib.base.repositories import BaseRepository


class LibraryBookRepository(BaseRepository):
    model_class = LibraryBook

    @classmethod
    def find_by_user(cls, user: User, offset, limit) -> List[LibraryBook]:
        return LibraryBook.objects.filter(user=user)[offset:offset + limit]

    @classmethod
    def get_by_user_and_book_id(cls, user: User, book_id: int) -> LibraryBook:
        return LibraryBook.objects.get(user=user, book_id=book_id)
