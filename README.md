# 💰 Money Control – Moliyaviy boshqaruv tizimi

**Money Control** – bu foydalanuvchilarga o‘z daromad va xarajatlarini boshqarish, kuzatish va tahlil qilish imkonini beruvchi **Django** asosidagi web-ilova.  
Loyiha foydalanuvchi uchun qulay **dashboard**, **kategoriya bo‘yicha kuzatuv**, va **grafik tahlil** imkoniyatlarini taqdim etadi.  

---

## ✨ Imkoniyatlar
- 🔑 **Login / Register** – foydalanuvchilar uchun xavfsiz ro‘yxatdan o‘tish va kirish  
- 🏦 **Kirim va chiqimlarni kiritish** – real vaqtda balansni ko‘rish  
- 📊 **Grafik va diagrammalar** – moliyaviy faoliyatni vizual ko‘rish  
- 🗂️ **Kategoriyalar bo‘yicha boshqaruv** – xarajat va daromadlarni toifalash  
- 🌍 **Til tanlash (i18n)** – O‘zbekcha, Ruscha, Inglizcha qo‘llab-quvvatlash  
- 🌙 **Dark Mode** – qulay dizayn rejimi  
- 🔒 **Xavfsizlik** – foydalanuvchi ma’lumotlari himoyalangan  

---

## 🛠 Texnologiyalar
- [Python 3.12+](https://www.python.org/)  
- [Django 5](https://www.djangoproject.com/)  
- [Bootstrap 5 / TailwindCSS](https://getbootstrap.com/) – dizayn uchun  
- [Chart.js](https://www.chartjs.org/) – grafiklar uchun  
- SQLite (default) yoki PostgreSQL (production uchun)  

---

## 🚀 O‘rnatish
```bash
git clone https://github.com/USERNAME/money-control.git
cd money-control

# Virtual environment yaratish
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py migrate

# Superuser yaratish
python manage.py createsuperuser

# Statik fayllarni yig‘ish
python manage.py collectstatic

# Serverni ishga tushirish
python manage.py runserver
