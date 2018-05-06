from allauth import urls as allauth_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.domains.account import urls as account_urls
from apps.domains.book import urls as book_urls
from apps.domains.home import urls as home_urls
from apps.domains.library.book import urls as library_book_urls

urlpatterns = [
  path('', include(home_urls, namespace='home')),
  path('admin/', admin.site.urls),
  path('accounts/', include(allauth_urls)),
  path('accounts/me/', include(account_urls)),
] + [
  path('api/library/books/', include(library_book_urls, namespace='library_book')),
  path('api/books/', include(book_urls, namespace='book')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
