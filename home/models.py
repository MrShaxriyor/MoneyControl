from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from income.models import Category
from django.conf import settings

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("income", "Kirim"),
        ("expense", "Chiqim"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"