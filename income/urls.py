from django.urls import path
from .views import income

urlpatterns = [
    path('income/', income, name="income"),
]
