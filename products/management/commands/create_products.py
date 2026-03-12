from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = "Створює 5 категорій та 12 продуктів ігор"

    def handle(self, *args, **options):
        categories_data = [
            {
                "name": "Настільні ігри",
                "icon": "🎲",
                "description": "Класичні настільні ігри для всієї родини.",
            },
            {
                "name": "Рольові ігри",
                "icon": "🧙‍♂️",
                "description": "Ігри для занурення у фантастичні світи.",
            },
            {
                "name": "Карткові ігри",
                "icon": "🃏",
                "description": "Ігри з картами для компанії.",
            },
            {
                "name": "Кооперативні ігри",
                "icon": "🤝",
                "description": "Ігри для командної роботи.",
            },
            {
                "name": "Стратегічні ігри",
                "icon": "♟️",
                "description": "Ігри для розвитку мислення та стратегії.",
            },
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={
                    "icon": cat_data["icon"],
                    "description": cat_data["description"],
                },
            )
            categories.append(category)

        products_data = [
            {
                "name": "Монополія",
                "category": categories[0],
                "description": "Класична економічна гра.",
                "price": 899.99,
                "rating": 8,
                "min_players": 2,
                "max_players": 6,
                "play_time": 120,
                "age_recommendation": 8,
                "image": "products/monopoly.jpg",
            },
            {
                "name": "Каркассон",
                "category": categories[0],
                "description": "Будуйте міста та дороги.",
                "price": 749.00,
                "rating": 9,
                "min_players": 2,
                "max_players": 5,
                "play_time": 45,
                "age_recommendation": 7,
                "image": "products/carcasson.jpg",
            },
            {
                "name": "Діксіт",
                "category": categories[2],
                "description": "Карткова гра на асоціації.",
                "price": 650.00,
                "rating": 8,
                "min_players": 3,
                "max_players": 6,
                "play_time": 30,
                "age_recommendation": 8,
                "image": "products/dixit.jpeg",
            },
            {
                "name": "Манчкін",
                "category": categories[1],
                "description": "Рольова гра з гумором.",
                "price": 499.00,
                "rating": 7,
                "min_players": 3,
                "max_players": 6,
                "play_time": 60,
                "age_recommendation": 10,
                "image": "products/manchkin.jpg",
            },
            {
                "name": "Колонізатори",
                "category": categories[4],
                "description": "Стратегічна гра про освоєння острова.",
                "price": 999.00,
                "rating": 9,
                "min_players": 3,
                "max_players": 4,
                "play_time": 90,
                "age_recommendation": 10,
                "image": "products/catan.jpg",
            },
            {
                "name": "Уно",
                "category": categories[2],
                "description": "Популярна карткова гра.",
                "price": 199.00,
                "rating": 8,
                "min_players": 2,
                "max_players": 10,
                "play_time": 20,
                "age_recommendation": 7,
                "image": "products/uno.jpeg",
            },
            {
                "name": "Пандемія",
                "category": categories[3],
                "description": "Кооперативна гра про боротьбу з вірусами.",
                "price": 850.00,
                "rating": 9,
                "min_players": 2,
                "max_players": 4,
                "play_time": 45,
                "age_recommendation": 8,
                "image": "products/pandemy.jpg",
            },
            {
                "name": "Еволюція",
                "category": categories[4],
                "description": "Стратегічна гра про розвиток видів.",
                "price": 700.00,
                "rating": 8,
                "min_players": 2,
                "max_players": 6,
                "play_time": 60,
                "age_recommendation": 12,
                "image": "products/evolution.jpg",
            },
            {
                "name": "Кодові імена",
                "category": categories[3],
                "description": "Кооперативна гра на асоціації.",
                "price": 400.00,
                "rating": 8,
                "min_players": 2,
                "max_players": 8,
                "play_time": 15,
                "age_recommendation": 10,
                "image": "",
            },
            {
                "name": "Дженга",
                "category": categories[0],
                "description": "Гра на спритність та уважність.",
                "price": 350.00,
                "rating": 7,
                "min_players": 2,
                "max_players": 8,
                "play_time": 20,
                "age_recommendation": 6,
                "image": "products/djenga.webp",
            },
            {
                "name": "Дракони і Підземелля",
                "category": categories[1],
                "description": "Класична рольова гра.",
                "price": 1200.00,
                "rating": 10,
                "min_players": 2,
                "max_players": 6,
                "play_time": 180,
                "age_recommendation": 14,
                "image": "products/Dungeons_and_Dragons.jpg",
            },
            {
                "name": "7 чудес",
                "category": categories[4],
                "description": "Стратегічна гра про цивілізації.",
                "price": 950.00,
                "rating": 9,
                "min_players": 2,
                "max_players": 7,
                "play_time": 30,
                "age_recommendation": 10,
                "image": "products/7wonders.jpeg",
            },
        ]

        for prod_data in products_data:
            product, created = Product.objects.get_or_create(
                name=prod_data["name"],
                defaults={
                    "category": prod_data["category"],
                    "description": prod_data["description"],
                    "price": prod_data["price"],
                    "rating": prod_data["rating"],
                    "min_players": prod_data["min_players"],
                    "max_players": prod_data["max_players"],
                    "play_time": prod_data["play_time"],
                    "age_recommendation": prod_data["age_recommendation"],
                    "image": prod_data["image"],
                },
            )
            if not created and not product.image and prod_data["image"]:
                product.image = prod_data["image"]
                product.save()

        self.stdout.write(self.style.SUCCESS("5 категорій та 12 продуктів створено!"))
