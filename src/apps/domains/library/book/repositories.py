from typing import List

from apps.domains.library.book.models import LibraryBook
from lib.base.repositories import BaseRepository


class LibraryBookRepository(BaseRepository):
    model_class = LibraryBook

    @classmethod
    def find_by_user(cls, user, offset, limit) -> List[LibraryBook]:
        return LibraryBook.objects.filter(user=user)[offset:offset+limit]
