import uuid
from urllib.error import HTTPError
from urllib.request import urlopen

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.management import BaseCommand

from apps.domains.book.constants import BookImageSourceType, BookImageType
from apps.domains.book.models import Book, BookImage


class Command(BaseCommand):
    title = 'Save book cover'
    help = 'Save book cover'

    def handle(self, *args, **options) -> None:
        books = Book.objects.filter(save_cover=False)[0:10000]

        for book in books:
            url = self.remove_query_string(book.cover_url)

            file_name = uuid.uuid4().hex + '.jpg'

            try:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(url).read())
                img_temp.flush()
            except HTTPError:
                print(url)
                continue

            book_image = BookImage(
                book_id=book.id, image_type=BookImageType.FRONT_COVER, source_type=BookImageSourceType.NAVER, source_url=url
            )
            book_image.file.save(file_name, File(img_temp))

            book.front_cover = book_image
            book.save_cover = True
            book.save()

    @staticmethod
    def remove_query_string(url: str) -> str:
        return url.split('?')[0]
