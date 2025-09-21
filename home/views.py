
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from income.models import Income, Category
from outgoing.models import Expense
from users.models import Balance
from decimal import Decimal
from django.db.models import Sum
from django.utils import timezone
from home.models import Transaction
from django.db.models.functions import ExtractMonth
from django.contrib.auth.models import User



@login_required
def get_home(request):
    user = request.user
    today = timezone.now().date()

    total_income = Income.objects.filter(user=user, date__date=today).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Expense.objects.filter(user=user, date__date=today).aggregate(Sum('amount'))['amount__sum'] or 0

    balance = Balance.objects.filter(user=user).first()
    current_balance = balance.amount if balance else 0
    currency = balance.currency if balance else "UZS"

    incomes = Income.objects.filter(user=user).values('id', 'date', 'amount', 'category__name', 'note')
    expenses = Expense.objects.filter(user=user).values('id', 'date', 'amount', 'category__name', 'note')

    transactions = []
    for i in incomes:
        transactions.append({
            "date": i["date"],
            "amount": i["amount"],
            "category": i["category__name"],
            "note": i["note"],
            "type": "income"
        })
    for e in expenses:
        transactions.append({
            "date": e["date"],
            "amount": e["amount"],
            "category": e["category__name"],
            "note": e["note"],
            "type": "expense"
        })

    recent_transactions = sorted(transactions, key=lambda x: x['date'], reverse=True)[:6]

    income_by_month_qs = Income.objects.filter(user=user).annotate(month=ExtractMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
    expense_by_month_qs = Expense.objects.filter(user=user).annotate(month=ExtractMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')

    months = list(range(1, 13))
    income_by_month = []
    expense_by_month = []

    income_dict = {item['month']: float(item['total']) for item in income_by_month_qs}
    expense_dict = {item['month']: float(item['total']) for item in expense_by_month_qs}

    for m in months:
        income_by_month.append(income_dict.get(m, 0))
        expense_by_month.append(expense_dict.get(m, 0))
    income_by_category = Income.objects.filter(user=user).values('category__name').annotate(total=Sum('amount')).order_by('-total')
    expense_by_category = Expense.objects.filter(user=user).values('category__name').annotate(total=Sum('amount')).order_by('-total')

    print("income_by_month:", list(income_by_month))
    print("expense_by_month:", list(expense_by_month))

    context = {
        "total_income": total_income,
        "total_expense": total_expense,
        "current_balance": current_balance,
        "currency": currency,
        "recent_transactions": recent_transactions,
        "income_by_month": income_by_month,
        "expense_by_month": expense_by_month,
        "income_by_category": list(income_by_category),
        "expense_by_category": list(expense_by_category),
        "categories": list(expense_by_category),
    }

    return render(request, "home.html", context)



def get_index(request):
    return render(request, 'index.html')
