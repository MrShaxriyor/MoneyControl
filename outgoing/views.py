from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Expense, Category
from users.models import Balance

@login_required
def expence(request):
    user = request.user
    today = timezone.now().date()
    today_expenses = Expense.objects.filter(user=user, date__date=today).order_by('-id')
    categories = Category.objects.all()

    if request.method == "POST":
        amount = request.POST.get('amount')
        category_id = request.POST.get('category')
        note = request.POST.get('note', '')

        if not amount or not category_id:
            messages.error(request, "Iltimos, summa va categoryni tanlang!")
            return redirect('expence')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, "Category topilmadi!")
            return redirect('expence')

        expense_instance = Expense.objects.create(
            user=user,
            amount=Decimal(amount),
            category=category,
            note=note,
            date=timezone.now()  
        )

        balance, created = Balance.objects.get_or_create(user=user)
        balance.amount -= Decimal(amount)
        balance.save()

        messages.success(request, "Chiqim muvaffaqiyatli qo‘shildi va balans yangilandi!")
        return redirect('dashboard')

    context = {
        'today_expenses': today_expenses,
        'categories': categories
    }
    return render(request, 'today_expense.html', context)



from django.conf import settings
from django.utils.translation import get_language

print("Current:", get_language())
print("Available:", settings.LANGUAGES)

