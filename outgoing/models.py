from django.db import models
from django.conf import settings
from income.models import Category
from django.utils import timezone


# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    currency = models.CharField(max_length=3, choices=[('UZS','UZS'),('USD','USD')], default='UZS')

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.category.name}"