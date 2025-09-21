from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import CustomUser


class Category(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    currency = models.CharField(max_length=3, choices=[('UZS','UZS'),('USD','USD')], default='UZS')

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.category.name}"