from django.core.management import BaseCommand

from apps.domains.book.services.new_book_service import NewBookService


class Command(BaseCommand):
    title = 'Crawling new books'
    help = 'Crawling new books'

    def handle(self, *args, **options) -> None:
        NewBookService.persist_new_books()
