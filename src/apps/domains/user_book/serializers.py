from apps.domains.user_book.models import UserBook
from lib.base.serializers import BaseModelSerializer, BasePaginatorReqSerializer


class UserBookSerializer(BaseModelSerializer):
    class Meta:
        model = UserBook
        fields = ('id', 'user', 'book', 'own_status', 'own_date', 'read_status', 'read_date', 'last_modified',)


class UserBookListReqSerializer(BasePaginatorReqSerializer):
    default_offset = 0
    default_limit = 100
