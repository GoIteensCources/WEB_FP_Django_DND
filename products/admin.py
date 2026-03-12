from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "icon", "description")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "name",
        "category",
        "price",
        "rating",
        "min_players",
        "max_players",
        "play_time",
        "age_recommendation",
    )
    list_filter = (
        "category",
        "rating",
        "min_players",
        "max_players",
        "play_time",
        "age_recommendation",
    )
    search_fields = ("name", "description")
