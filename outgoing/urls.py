from django.urls import path
from .views import expence

urlpatterns = [
    
    path('expence/', expence, name='expence')
]
