from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return self.username



class Balance(models.Model):
    CURRENCY_CHOICES = [
        ('UZS', 'UZS'),
        ('USD', 'USD'),
    ]

    METHOD_CHOICES = [
        ('visa', 'Visa'),
        ('uzcard_humo', 'UzCard/Humo'),
        ('wallet', 'Hamyon'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='UZS')
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    account_number = models.CharField(max_length=50, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} {self.currency}"
