from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = "products"

    def ready(self):
        import products.signals  # Імпортуємо сигнали для кешування категорій
