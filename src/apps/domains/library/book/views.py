from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from apps.domains.book.models import Book
from apps.domains.library.book.repositories import LibraryBookRepository
from apps.domains.library.book.serializers import LibraryBookListReqSerializer, LibraryBookSerializer
from apps.domains.library.book.services.library_book_own_service import LibraryBookOwnService
from apps.domains.library.book.services.library_book_read_service import LibraryBookReadService

from infra.networks.api_status_code import ApiStatusCodes
from lib.base.views import ApiResponseMixin


class LibraryBookListView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user

        serializer = LibraryBookListReqSerializer(data=request.query_params)
        if not serializer.is_valid():
            code = self.make_response_code(ApiStatusCodes.C_400_BAD_REQUEST)
            return self.fail_response(response_code=code, data=serializer.errors)

        offset, limit = serializer.get_paginator_params()
        user_books = LibraryBookRepository.find_by_user(user, offset, limit)

        data = {
            'user_books': LibraryBookSerializer(user_books, many=True).data,
        }

        return self.success_response(data=data)


class ReadView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, book_id: int, read_status: int):
        user = request.user

        try:
            LibraryBookReadService.change_read_status(user, book_id, read_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()


class OwnView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, book_id: int, own_status: int):
        user = request.user

        try:
            LibraryBookOwnService.change_own_status(user, book_id, own_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()


class ISBNReadView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, isbn: int, read_status: int):
        user = request.user

        try:
            LibraryBookReadService.change_read_status_by_isbn(user, isbn, read_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()


class ISBNOwnView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, isbn: int, own_status: int):
        user = request.user

        try:
            LibraryBookOwnService.change_own_status_by_isbn(user, isbn, own_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()
