from django.urls import path

from ..views import www as views

app_name = 'apps.domains.library.book'
urlpatterns = [
    path('', views.LibraryBookListView.as_view(), name='index'),
    path('search/<str:keyword>/', views.BookByKeywordView.as_view(), name='by-keyword'),
]
