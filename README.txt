Прізвище, ім'я, група: ______________________
Тема: 4 — Кінотеатр (додатки cinema та accounts)

Запуск: py -m venv venv → venv\Scripts\activate → pip install -r requirements.txt
        → py manage.py runserver
Сайт: http://127.0.0.1:8000/   Адмін-панель: http://127.0.0.1:8000/admin/

Акаунти:
  admin   (суперкористувач) / Admin12345!
  manager (is_staff)        / Manager12345!
  client  (звичайний)       / Client12345!

Виконано (Частина A):
  - проєкт, налаштування (uk, Europe/Kyiv, LOGIN_URL та ін.), requirements.txt
  - 4 моделі (Hall, Genre, Screening, Ticket), міграції, адмін-панель
  - сторінки: головна, афіша, деталі, список залів, сторінка залу
  - CRUD сеансів (ModelForm, csrf, redirect, messages, валідації clean_price, clean_age_limit)
  - публічна форма квитків (clean_phone, перевірка вільних місць), список квитків для персоналу
  - реєстрація, вхід, вихід (POST), ?next=
  - декоратор staff_required (403 для не-персоналу), приховані кнопки
  - спеціальна функціональність: пошук ?q= + фільтр ?genre= разом, free_seats(), сторінка залу

Не виконано або відомі проблеми: немає.

Виконано (Частина B): не виконувалась.
