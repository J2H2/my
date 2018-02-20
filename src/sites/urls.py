from allauth import urls as allauth_urls
from django.contrib import admin
from django.urls import include, path

from apps.domains.home import urls as home_urls

urlpatterns = [
    path('', include(home_urls, namespace='home')),
    path('admin/', admin.site.urls),
    path('accounts/', include(allauth_urls)),
]
