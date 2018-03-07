from typing import List

from apps.domains.book.models import Book
from lib.naver.api import search_book


class SearchBookService:
    @staticmethod
    def find_books(keyword: str) -> List[Book]:
        _books = []
        result = search_book(keyword)
        for item in result.items:
            _books = Book.objects.get_or_create(
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

        return _books

    @classmethod
    def find_by_books_property(cls, books: List[Book]) -> List[Book]:
        _books = []
        for book in books:
            _books += cls.find_by_book_property(book)
        return _books

    @classmethod
    def find_by_book_property(cls, book: Book) -> List[Book]:
        _books = []
        _books += cls.find_books(book.title)
        _books += cls.find_books(book.authors)
        _books += cls.find_books(book.publisher)
        return _books
