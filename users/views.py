
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Balance
from django.contrib.auth import update_session_auth_hash
from django.utils.translation import gettext as _
from .models import CustomUser
from income.models import  Category

User = get_user_model()


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Parollar mos emas!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu username allaqachon mavjud!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon mavjud!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        login(request, user)
        messages.success(request, f"Success Register, {username}!")
        return redirect('login')

    return render(request, 'auth/register.html')



def get_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            messages.error(request, "Email yoki parol noto‘g‘ri!")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Email yoki parol noto‘g‘ri!")
            return redirect('login')

    return render(request, 'auth/login.html')


@login_required
def balance(request):
    user = request.user

    try:
        user_balance = Balance.objects.get(user=user)
    except Balance.DoesNotExist:
        user_balance = None

    if request.method == "POST":
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        method = request.POST.get('method')
        account_number = request.POST.get('account_number')

        if not all([amount, currency, method, account_number]):
            messages.error(request, "Iltimos, barcha maydonlarni to‘ldiring!")
            return redirect('balance')

        if user_balance:
            user_balance.amount = float(amount)
            user_balance.currency = currency
            user_balance.method = method
            user_balance.account_number = account_number
            user_balance.save()
            messages.success(request, "Balans muvaffaqiyatli yangilandi!")
        else:
            Balance.objects.create(
                user=user,
                amount=float(amount),
                currency=currency,
                method=method,
                account_number=account_number
            )
            messages.success(request, "Balans muvaffaqiyatli yaratildi!")

        return redirect('balance')

    context = {
        'balance': user_balance
    }
    return render(request, 'balance.html', context)

def history(request):
    return render(request, 'history.html')

@login_required
def sozlama(request):
    user = request.user

    if request.method == "POST":
        tab = request.POST.get('tab', 'profile')

        if tab == 'profile':
            user.first_name = request.POST.get('first_name', user.first_name)
            user.last_name = request.POST.get('last_name', user.last_name)
            user.email = request.POST.get('email', user.email)
            user.phone = request.POST.get('phone', user.phone)
            user.save()
            messages.success(request, "Shaxsiy ma’lumotlar saqlandi!")

        elif tab == 'account':
            balance = Balance.objects.filter(user=request.user).first()
            if balance is not None:
                balance.currency = request.POST.get('currency', balance.currency)
                balance.save()
                messages.success(request, "Hisob ma’lumotlari saqlandi!")
            else:
                messages.error(request, "Sizning balansingiz topilmadi!")

        elif tab == 'security':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password and new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Parol muvaffaqiyatli o‘zgartirildi!")
            else:
                messages.error(request, "Parollar mos kelmadi!")

        return redirect('dashboard')

    context = {
        "user": user,
    }
    return render(request, "sozlama.html", context)

@login_required
def category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Category.objects.create(user=request.user, name=name)
            messages.success(request, f"Kategoriya '{name}' muvaffaqiyatli qo‘shildi!")
            return redirect("dashboard")
        else:
            messages.error(request, "Kategoriya nomini kiritishingiz kerak!")

    categories = Category.objects.filter(user=request.user)
    return render(request, "category.html", {"categories": categories})


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("home") 
