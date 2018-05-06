from apps.domains.library.book.models import LibraryBook
from lib.base.serializers import BaseModelSerializer, BasePaginatorReqSerializer


class LibraryBookSerializer(BaseModelSerializer):
    class Meta:
        model = LibraryBook
        fields = ('id', 'user', 'book', 'own_status', 'own_date', 'read_status', 'read_date', 'last_modified',)


class LibraryBookListReqSerializer(BasePaginatorReqSerializer):
    default_offset = 0
    default_limit = 100
