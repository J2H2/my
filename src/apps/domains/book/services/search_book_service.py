from typing import List

from django.db import OperationalError

from apps.domains.book.models import Book
from lib.naver.api import search_book


class SearchBookService:
    @staticmethod
    def find_books(keyword: str) -> List[Book]:
        books = []
        result = search_book(keyword)
        for item in result.items:
            try:
                book, _ = Book.objects.get_or_create(
                    isbn=item.isbn,
                    defaults={
                        'title': item.title,
                        'cover_s': item.image,
                        'authors': item.author,
                        'publisher': item.publisher,
                        'description': item.description,
                        'pub_date': item.pubdate,
                        'price': item.price,
                    }
                )
            except OperationalError:
                # TODO logger 추가
                # TODO desc 에 mb4형식이 있을 수 있음. desc 정리를 하거나 DB설정을 바꾸거나 해야 함
                continue
            books.append(book)

        return books

    @classmethod
    def find_by_books_property(cls, books: List[Book]) -> List[Book]:
        target_books = []
        for book in books:
            target_books += cls.find_by_book_property(book)
        return target_books

    @classmethod
    def find_by_book_property(cls, book: Book) -> List[Book]:
        books = []
        books += cls.find_books(book.title)
        books += cls.find_books(book.authors)
        books += cls.find_books(book.publisher)
        return books
