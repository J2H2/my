from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from apps.domains.account.services.token_service import TokenService
from apps.domains.book.models import Book
from apps.domains.book.services.search_book_service import SearchBookService
from apps.domains.library.book.repositories import LibraryBookRepository


class LibraryBookListView(View):
    @method_decorator(login_required)
    def get(self, request):
        user = request.user

        user_books = LibraryBookRepository.find_all_by_user(user)

        context = {
            'user_books': user_books,
        }

        return render(request, 'library/book/index.html', context)


class BookByKeywordView(View):
    @method_decorator(login_required)
    def get(self, request, keyword: str):
        try:
            books = SearchBookService.find_books(keyword)

        except Book.DoesNotExist:
            books = []

        context = {
            'books': books,
            'token': TokenService.get_token(request.user)
        }

        return render(request, 'library/book/index.html', context)

