from django.urls import path

from .views import get_home, get_index

urlpatterns = [
    path('dashboard/', get_home, name="dashboard"),
    path('', get_index, name="home"),
]

