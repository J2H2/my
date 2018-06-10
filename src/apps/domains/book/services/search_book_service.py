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
                        'cover_url': item.image,
                        'authors': item.author,
                        'publisher': item.publisher,
                        'description': item.description,
                        'pub_date': item.pubdate,
                        'price': item.price,
                    }
                )
            except OperationalError:
                # TODO Add logger
                # TODO There can be mb4 format in desc. Need to clean up your desc or change DB settings
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
