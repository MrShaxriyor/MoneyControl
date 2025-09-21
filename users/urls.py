from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, get_login, balance, history, sozlama, category, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path("logout/", logout_view, name="logout"),
    path('login/', get_login, name='login'),
    path('balance/', balance, name='balance'),
    path('history/', history, name='history'),
    path('sozlama/', sozlama, name='sozlama'),
    path('category/', category, name='category'),
]
