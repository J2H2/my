from django.urls import path
from . import views

app_name = 'apps.domains.home'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
