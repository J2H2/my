from django.urls import path

from . import views

app_name = 'apps.domains.book'
urlpatterns = [
    path('<int:book_id>/', views.BookByIdView.as_view(), name='by-id'),
    path('isbn/<int:isbn>/', views.BookByIsbnView.as_view(), name='by-isbn'),
    path('search/<str:keyword>/', views.BookByKeywordView.as_view(), name='by-keyword'),
]
