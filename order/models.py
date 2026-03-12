from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ("new", "Новий"),
        ("processing", "В обробці"),
        ("shipped", "Відправлений"),
        ("completed", "Завершений успішно"),
        ("cancelled", "Скасований"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    shipping_name = models.CharField(max_length=100, verbose_name="Ім'я отримувача")
    shipping_city = models.CharField(max_length=100, verbose_name="Місто доставки")
    shipping_street = models.CharField(max_length=255, verbose_name="Вулиця доставки")
    shipping_zip_code = models.CharField(
        max_length=20, verbose_name="Поштовий індекс доставки"
    )
    shipping_country = models.CharField(max_length=100, verbose_name="Країна доставки")

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    coment = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Замовлення #{self.id} від {self.shipping_name} {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    @property
    def total_price(self) -> float:
        return self.product_price * self.quantity

    def __str__(self):
        return f"{self.product_name} (x{self.quantity}) - {self.product_price} грн"
