# Dice & Dragons

Фентезійний інтернет-магазин настільних ігор на Django. Стилізований під магічну крамницю — кожна категорія виглядає як гільдія, кожна гра — як артефакт з іншого світу.

## Стек

- Python 3.12
- Django 6.0.2
- SQLite
- HTML/CSS (кастомна fantasy-тема)

## Структура проєкту

```
Dice_N_Dragon/
├── dnd_project/        # Налаштування Django (settings, urls, wsgi)
├── products/           # Основний додаток
│   ├── models.py       # Category, Product
│   ├── views.py        # FBV + CBV
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── create_products.py  # Команда наповнення БД
├── account/            # Додаток для акаунтів
├── templates/          # HTML-шаблони
│   ├── base.html
│   ├── components/
│   └── projects/       # Шаблони магазину
├── static/
│   ├── dnd_fantasy.css
│   └── media/
│       └── products/   # Зображення товарів
└── manage.py
```

## Встановлення та запуск

```bash
# Клонувати репозиторій та перейти в папку
cd Dice_N_Dragon

# Створити та активувати віртуальне середовище
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Встановити залежності
pip install django pillow

# Застосувати міграції
python manage.py migrate

# Наповнити БД тестовими даними
python manage.py create_products

# Запустити сервер
python manage.py runserver
```

Відкрити у браузері: http://127.0.0.1:8000

## URL-маршрути

| URL | Опис |
|-----|------|
| `/` | Головна сторінка |
| `/categories/` | Список категорій (гільдій) |
| `/categories/<slug>/` | Ігри певної категорії |
| `/products/` | Каталог усіх ігор |
| `/products/<slug>/` | Картка товару |
| `/admin/` | Адмін-панель |

## Моделі

**Category** — категорія ігор
`name`, `slug`, `icon` (emoji), `description`

**Product** — настільна гра
`name`, `slug`, `category`, `description`, `price`, `rating`, `min_players`, `max_players`, `play_time`, `age_recommendation`, `image`

## Медіафайли

Зображення зберігаються у `static/media/products/`.
У `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static' / 'media'
```
