from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from apps.domains.book.models import Book
from apps.domains.user_book.models import UserBook
from apps.domains.user_book.serializers import UserBookSerializer
from apps.domains.user_book.services.user_book_own_service import UserBookOwnService
from apps.domains.user_book.services.user_book_read_service import UserBookReadService
from infra.networks.api_status_code import ApiStatusCodes
from lib.base.views import ApiResponseMixin


class UserBooksView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user

        user_books = UserBook.objects.filter(user=user)

        data = {
            'user_books': UserBookSerializer(user_books, many=True).data,
        }

        return self.success_response(data=data)


class ReadView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, book_id: int, read_status: int):
        user = request.user

        try:
            UserBookReadService.change_read_status(user, book_id, read_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()


class OwnView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, book_id: int, own_status: int):
        user = request.user

        try:
            UserBookOwnService.change_own_status(user, book_id, own_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()


class ISBNReadView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, isbn: int, read_status: int):
        user = request.user

        try:
            UserBookReadService.change_read_status_by_isbn(user, isbn, read_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()


class ISBNOwnView(ApiResponseMixin, APIView):
    @method_decorator(login_required)
    def post(self, request, isbn: int, own_status: int):
        user = request.user

        try:
            UserBookOwnService.change_own_status_by_isbn(user, isbn, own_status)

        except Book.DoesNotExist:
            code = self.make_response_code(ApiStatusCodes.C_404_NOT_FOUND, message='The book does not exist.')
            return self.fail_response(response_code=code)

        return self.success_response()
