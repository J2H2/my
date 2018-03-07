from apps.domains.book.services.search_book_service import SearchBookService
from lib.kyobo.crawling import get_new_books_isbn


class NewBookService:
    @classmethod
    def persist_new_books(cls):
        isbns = get_new_books_isbn()

        for isbn in isbns:
            books = SearchBookService.find_books(isbn)
            books += SearchBookService.find_by_books_property(books)

