from rest_framework.views import APIView

from apps.domains.book.models import Book
from apps.domains.book.serializers import BookSerializer
from apps.domains.book.services.book_service import BookService
from apps.domains.book.services.search_book_service import SearchBookService
from infra.networks.api_status_code import ApiStatusCodes
from lib.base.views import ApiResponseMixin


class BookByIdView(ApiResponseMixin, APIView):
    def get(self, request, book_id: int):
        try:
            book = BookService.get_book_by_id(book_id)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        data = {
            'books': [BookSerializer(book).data],
        }

        return self.success_response(data=data)


class BookByIsbnView(ApiResponseMixin, APIView):
    def get(self, request, isbn: int):
        try:
             book = BookService.get_book_by_isbn(isbn)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        data = {
            'books': [BookSerializer(book).data],
        }

        return self.success_response(data=data)


class BookByKeywordView(ApiResponseMixin, APIView):
    def get(self, request, keyword: str):
        try:
            book = SearchBookService.find_books(keyword)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        data = {
            'books': BookSerializer(book, many=True).data,
        }

        return self.success_response(data=data)
