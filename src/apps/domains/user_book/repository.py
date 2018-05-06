from typing import List

from apps.domains.user_book.models import UserBook
from lib.base.repository import BaseRepository


class UserBookRepository(BaseRepository):
    model_class = UserBook

    @classmethod
    def find_by_user(cls, user, offset, limit) -> List[UserBook]:
        return UserBook.objects.filter(user=user)[offset:offset+limit]
