# AI.md

## Project Overview

Dice & Dragons — a fantasy-themed Django board game shop. Ukrainian UI/content, English code. Products are organized into "guilds" (categories) with a magical grimoire aesthetic.

## Commands

```bash
# Activate venv
source .venv/bin/activate

# Run dev server (http://127.0.0.1:8000/)
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Populate DB with test data (safe to re-run, uses get_or_create)
python manage.py create_products

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```

## Architecture

**Framework:** Django 6.0.2, SQLite, Bootstrap 5.3.2

**Django Apps:**
- `products` — main app: Category and Product models, catalog views, admin config
- `account` — stub app for future user auth (not yet in INSTALLED_APPS)

**Project layout:**
- `dnd_project/` — Django project config (settings, root URLs)
- `products/` — models, views, URLs, admin, management commands
- `templates/` — base.html + components (header/footer) + page templates in `templates/projects/`
- `static/` — `dnd_fantasy.css` (fantasy theme) + media assets

**Key patterns:**
- Mixed FBV and CBV views (home/product views are FBV, category views are CBV ListView/DetailView)
- Auto-generated slugs on model save; all detail URLs use slugs, not IDs
- `select_related('category')` used in product queries for optimization
- Template inheritance: `base.html` → page templates; header/footer as `{% include %}` components
- Related name: `category.products.all()` to access products from a category

**URL structure:** Root includes `products.urls` at `/`. Admin at `/admin/`.

## Design System

Fantasy color scheme: dark purple (#4b206b), dark blue (#2a3a5a), gold (#d4af37), teal accent (#00e6b8), parchment backgrounds. Cinzel serif font for headers. Custom CSS in `static/dnd_fantasy.css`.
