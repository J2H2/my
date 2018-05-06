from django.urls import path

from . import views

app_name = 'apps.domains.account'
urlpatterns = [
    path('token/', views.TokenView.as_view(), name='token'),
]
