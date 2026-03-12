from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Emoji або іконка")
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Категорії"
        verbose_name = "Категорія"
        ordering = ["name"]

    def __str__(self):
        return f"{self.icon} {self.name}" if self.icon else self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    rating = models.IntegerField(default=0, help_text="Рейтинг від 0 до 10")

    # ХАрактеристики гри
    min_players = models.IntegerField(
        default=2, help_text="Мінімальна кількість гравців"
    )
    max_players = models.IntegerField(
        default=4, help_text="Максимальна кількість гравців"
    )
    play_time = models.IntegerField(default=60, help_text="Середній час гри в хвилинах")
    age_recommendation = models.IntegerField(
        default=12, help_text="Рекомендований вік гравців"
    )

    image = models.ImageField(upload_to="products/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Продукти"
        verbose_name = "Продукт"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Теги"
        verbose_name = "Тег"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
