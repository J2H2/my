from django.urls import path

from apps.domains.library.book.constants import OwnStatus, ReadStatus
from . import views

app_name = 'apps.domains.library.book'
urlpatterns = [
    path('', views.LibraryBookListView.as_view(), name='index'),
    path('<int:book_id>/', views.LibraryBookByBookIdView.as_view(), name='get-by-id',),
    path('isbn/<int:isbn>/', views.LibraryBookByIsbnView.as_view(), name='get-by-isbn',),

    path('<int:book_id>/not-own/', views.OwnView.as_view(), name='not-own', kwargs={'own_status': OwnStatus.NONE}),
    path('<int:book_id>/want/', views.OwnView.as_view(), name='want', kwargs={'own_status': OwnStatus.WANT}),
    path('<int:book_id>/own/', views.OwnView.as_view(), name='own', kwargs={'own_status': OwnStatus.OWN}),

    path('<int:book_id>/not-read/', views.ReadView.as_view(), name='not-read', kwargs={'read_status': ReadStatus.NONE}),
    path('<int:book_id>/reading/', views.ReadView.as_view(), name='reading', kwargs={'read_status': ReadStatus.READING}),
    path('<int:book_id>/read/', views.ReadView.as_view(), name='read', kwargs={'read_status': ReadStatus.READ}),

    path('isbn/<int:isbn>/not-own/', views.IsbnOwnView.as_view(), name='isbn-not-own', kwargs={'own_status': OwnStatus.NONE}),
    path('isbn/<int:isbn>/want/', views.IsbnOwnView.as_view(), name='isbn-want', kwargs={'own_status': OwnStatus.WANT}),
    path('isbn/<int:isbn>/own/', views.IsbnOwnView.as_view(), name='isbn-own', kwargs={'own_status': OwnStatus.OWN}),

    path('isbn/<int:isbn>/not-read/', views.IsbnReadView.as_view(), name='isbn-not-read', kwargs={'read_status': ReadStatus.NONE}),
    path('isbn/<int:isbn>/reading/', views.IsbnReadView.as_view(), name='isbn-reading', kwargs={'read_status': ReadStatus.READING}),
    path('isbn/<int:isbn>/read/', views.IsbnReadView.as_view(), name='isbn-read', kwargs={'read_status': ReadStatus.READ}),
]
