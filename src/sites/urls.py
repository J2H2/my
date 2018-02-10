from django.contrib import admin
from django.urls import path, include
from apps.domains.home import urls as home_urls

urlpatterns = [
    path('', include(home_urls, namespace='home')),
    path('admin/', admin.site.urls),
]
