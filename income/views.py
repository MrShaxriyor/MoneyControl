from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Income, Category
from users.models import Balance
from decimal import Decimal

@login_required
def income(request):
    user = request.user
    now = timezone.now()  # Sana + vaqt

    today_incomes = Income.objects.filter(user=user, date__date=now.date()).order_by('-date')
    categories = Category.objects.all()

    if request.method == "POST":
        amount = request.POST.get('amount')
        category_id = request.POST.get('category')
        note = request.POST.get('note', '')

        if not amount or not category_id:
            messages.error(request, "Iltimos, summa va categoryni tanlang!")
            return redirect('income')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, "Category topilmadi!")
            return redirect('income')

        income_instance = Income.objects.create(
            user=user,
            amount=Decimal(amount),
            category=category,
            note=note,
            date=now  # Bu yerda vaqt bilan saqlanadi
        )

        balance, created = Balance.objects.get_or_create(user=user)
        balance.amount += Decimal(amount)
        balance.save()

        messages.success(request, "Kirim muvaffaqiyatli qo‘shildi va balans yangilandi!")
        return redirect('income')

    context = {
        'today_incomes': today_incomes,
        'categories': categories
    }
    return render(request, 'today_income.html', context)
