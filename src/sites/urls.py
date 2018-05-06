from allauth import urls as allauth_urls
from django.contrib import admin
from django.urls import include, path

from apps.domains.home import urls as home_urls
from apps.domains.user_book import urls as book_urls

urlpatterns = [
    path('', include(home_urls, namespace='home')),
    path('admin/', admin.site.urls),
    path('accounts/', include(allauth_urls)),
] + [
    path('api/books/', include(book_urls, namespace='user_book')),
]
