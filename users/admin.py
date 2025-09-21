from django.contrib import admin
from .models import CustomUser, Balance
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Balance)