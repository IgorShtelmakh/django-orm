# Інструкція з запуску Django ORM проекту

## Передумови
- Python 3.8+ встановлено
- Віртуальне середовище створено

## Кроки для запуску

### 1. Активація віртуального середовища

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 2. Встановлення залежностей (якщо необхідно)
```bash
pip install -r requirements.txt
```

### 3. Застосування міграцій (вже виконано)
```bash
python manage.py migrate
```

### 4. Наповнення БД демонстраційними даними (вже виконано)
```bash
python manage.py seed
```

### 5. Створення суперкористувача для адмін-панелі
```bash
python manage.py createsuperuser
```

Введіть:
- Username: admin
- Email: admin@example.com
- Password: (ваш пароль)

### 6. Запуск сервера розробки
```bash
python manage.py runserver
```

### 7. Доступ до адмін-панелі
Відкрийте браузер та перейдіть за адресою:
```
http://127.0.0.1:8000/admin/
```

Увійдіть з обліковими даними суперкористувача.

## Структура проекту

```
django-orm/
├── shop/                          # Головний проект Django
│   ├── settings.py               # Налаштування проекту
│   ├── urls.py                   # URL маршрути
│   └── ...
├── store/                         # Додаток магазину
│   ├── models/                   # Моделі (організовані у окремі файли)
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── supplier.py
│   │   ├── product.py
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── shipment.py
│   ├── admin/                    # Адмін-панель (організована у окремі файли)
│   │   ├── __init__.py
│   │   ├── category.py
│   │   ├── supplier.py
│   │   ├── product.py
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── shipment.py
│   ├── management/               # Кастомні команди
│   │   └── commands/
│   │       └── seed.py          # Команда для наповнення БД
│   └── migrations/               # Міграції бази даних
├── manage.py                     # CLI для управління проектом
├── db.sqlite3                    # База даних SQLite
└── venv/                         # Віртуальне середовище Python
```

## Корисні команди Django ORM

### Робота з Django Shell
```bash
python manage.py shell
```

### Приклади запитів ORM

```python
from store.models import *

# Отримати всі категорії
Category.objects.all()

# Знайти товар за артикулом
Product.objects.get(sku='LAP001')

# Отримати всі товари категорії "Ноутбуки"
Product.objects.filter(category__name='Ноутбуки')

# Отримати товари дорожче 30000 грн
Product.objects.filter(list_price__gt=30000)

# Отримати всі замовлення конкретного клієнта
customer = Customer.objects.get(email='ivan.petrenko@example.com')
customer.orders.all()

# Підрахунок кількості товарів у категорії
category = Category.objects.get(name='Смартфони')
category.products.count()
```

## Статистика БД

- **Категорій**: 8
- **Постачальників**: 5
- **Товарів**: 10
- **Клієнтів**: 5
- **Адрес**: 10
- **Замовлень**: 12
- **Позицій замовлення**: 31
- **Платежів**: 12
- **Відправлень**: 6

## Додаткова інформація

Всі моделі включають:
- Валідацію даних
- Зручні verbose_name для адмін-панелі
- Методи __str__ для зручного відображення
- Related_name для зворотніх зв'язків
- Правильні on_delete поведінки

Адміністративна панель включає:
- Фільтри та пошук
- Inline редагування зв'язаних об'єктів
- Кастомні поля з кольоровим відображенням
- Сортування та пагінацію
