# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Dice & Dragons** — a fantasy-themed Django board game shop. Ukrainian UI/content, English code. The aesthetic is a magical grimoire/wizard's shop.

## Commands

```bash
# Activate virtual environment (required before any manage.py commands)
source .venv/bin/activate

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

**Stack:** Django 6.0.2, Python 3.12, SQLite, Bootstrap 5.3.2, Pillow

### Django Apps

- **`products`** — core catalog: `Category` and `Product` models, views, admin, and the `create_products` management command
- **`account`** — user auth: `Profile` and `Address` models extending Django's built-in `User`; signals auto-create `Profile`+`Address` on `User` creation (wired via `AccountConfig.ready()`)
- **`card`** — shopping cart: `Cart` (OneToOne to User) and `CartItem` models; supports authenticated (database-persisted) and guest (session-based) users; `context_processor.py` provides `{{ cart_item_count }}` globally
- **`order`** — placeholder app (empty models/views), checkout not yet implemented

### URL Namespaces

| Namespace | Prefix | Key routes |
|-----------|--------|------------|
| `products` | `/` | `home`, `categories_list`, `category`, `product_list`, `product_details`, `search` |
| `account` | `/account/` | `login`, `logout`, `register`, `profile`, `edit_profile`, `delete_profile` |
| `card` | `/card/` | `cart_details`, `add_cart`, `remove_from_cart`, `update_cart` |

### Models

**`Category`:** `name`, `slug` (auto-generated), `icon` (emoji), `description`

**`Product`:** `name`, `slug`, `category` (FK), `description`, `price`, `rating`, `min_players`, `max_players`, `play_time`, `age_recommendation`, `image`

**`Profile`:** OneToOne with `User`; `phone_number`, FK to `Address`

**`Address`:** FK to `User`; `street`, `city`, `postal_code`, `country`

**`Cart`:** OneToOne with `User`; related items via `CartItem`

**`CartItem`:** FK to `Cart` and `Product`; `quantity`

### Key Patterns

- **Slugs:** Auto-generated on `save()` using `slugify(name, allow_unicode=True)` if not set. All detail URLs use slugs, not IDs.
- **Views:** Mixed FBV (`home`, `product_list`, `product_details`, `product_search`, all account views, all cart views) and CBV (`CategoryListView`, `CategoryDetailView`).
- **Dual cart storage:** `card/views.py` checks `request.user.is_authenticated` — authenticated users get DB-backed `Cart`/`CartItem`, guests use `request.session['cart']` as a `{product_id: quantity}` dict.
- **Query optimization:** `select_related('category')` in product list/detail views; `select_related('product')` in cart item retrieval.
- **Templates:** `base.html` → page templates; header/footer as `{% include %}` components. Product pages in `templates/projects/`, account pages in `templates/accounts/`, cart in `templates/cart/`.
- **Signals:** `account/signals.py` imported in `AccountConfig.ready()` — auto-creates `Profile` and `Address` when a `User` is created.
- **Message tags:** `MESSAGE_TAGS` maps `ERROR` → `'danger'` for Bootstrap compatibility.

### Static & Media

`MEDIA_ROOT` is `BASE_DIR / "static" / "media"` (media lives inside `static/`). Product images at `static/media/products/`. Served via `urlpatterns += static(...)` in development.

### Design System

Fantasy color scheme: dark purple `#4b206b`, dark blue `#2a3a5a`, gold `#d4af37`, teal `#00e6b8`. Cinzel serif font for headers. All custom styles in `static/dnd_fantasy.css`.
