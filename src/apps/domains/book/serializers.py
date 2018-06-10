from apps.domains.book.models import Book
from lib.base.serializers import BaseModelSerializer


class BookSerializer(BaseModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'isbn', 'title', 'authors', 'publisher', 'pub_date', 'cover_url', )
