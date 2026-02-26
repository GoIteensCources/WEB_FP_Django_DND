# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Dice & Dragons** — a fantasy-themed Django board game shop. Ukrainian UI/content, English code. Categories are called "guilds"; the aesthetic is a magical grimoire/wizard's shop.

## Commands

```bash
# Activate virtual environment (required before any manage.py commands)
source .venv/bin/activate

# Install dependencies (only django and pillow are needed)
pip install django pillow

# Run development server
python manage.py runserver

# Migrations
python manage.py makemigrations
python manage.py migrate

# Populate DB with sample board game data (idempotent — uses get_or_create)
python manage.py create_products

# Run tests
python manage.py test                         # all tests
python manage.py test products                # single app
python manage.py test products.tests.MyTest   # single test class
```

## Architecture

**Stack:** Django 6.0.2, Python 3.12, SQLite, Bootstrap 5.3.2

### Django Apps

- **`products`** — core catalog: `Category` and `Product` models, views, URLs, admin, and the `create_products` management command
- **`account`** — user auth: `Profile` and `Address` models extending Django's built-in `User`; signals auto-create `Profile`+`Address` on `User` creation (wired via `AccountConfig.ready()`)
- **`card`** — shopping basket; currently a stub (empty models/views/urlpatterns), next to be implemented

### URL Namespaces

| Namespace | Prefix | Key routes |
|-----------|--------|------------|
| `products` | `/` | `home`, `categories_list`, `category`, `product_list`, `product_details`, `search` |
| `account` | `/account/` | `login`, `logout`, `register`, `profile`, `edit_profile`, `delete_profile` |
| `card` | `/card/` | (empty — to be built) |

### Models

**`Category`:** `name`, `slug` (auto-generated), `icon` (emoji), `description`
- Related name to products: `category.products.all()`

**`Product`:** `name`, `slug` (auto-generated), `category` (FK), `description`, `price`, `rating`, `min_players`, `max_players`, `play_time`, `age_recommendation`, `image`

**`Profile`:** OneToOne with `User`; has `phone_number` and FK to `Address`

**`Address`:** FK to `User`; `street`, `city`, `postal_code`, `country`

### Key Patterns

- **Slugs:** Auto-generated on `save()` using `slugify(name, allow_unicode=True)` if not set. All detail URLs use slugs, not IDs.
- **Views:** Mixed FBV (`home`, `product_list`, `product_details`, `product_search`) and CBV (`CategoryListView`, `CategoryDetailView`). Account views are all FBV.
- **Query optimization:** `select_related('category')` used in product list/detail views.
- **Templates:** `base.html` → page templates; header/footer as `{% include %}` components. Product pages live in `templates/projects/`, account pages in `templates/accounts/`.
- **Signals:** `account/signals.py` imported in `AccountConfig.ready()` — auto-creates `Profile` and `Address` when a `User` is created.

### Static & Media

`MEDIA_ROOT` is set to `BASE_DIR / "static" / "media"` (media files live inside the `static/` directory). Product images are stored at `static/media/products/`. In development, media is served via `urlpatterns += static(...)` in `dnd_project/urls.py`.

### Design System

Fantasy color scheme: dark purple `#4b206b`, dark blue `#2a3a5a`, gold `#d4af37`, teal `#00e6b8`, parchment backgrounds. Cinzel serif font for headers. All custom styles in `static/dnd_fantasy.css`.
