from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.core.cache import cache
from django_ratelimit.decorators import ratelimit


CATEGORY_CACHE_KEY = "categories_cache"
CATEGOTY_CACHE_TTL = 60 * 60 * 12  # 1 година


@ratelimit(key="ip", rate="100/m", method="GET", block=True)
def home(request):
    best_products = Product.objects.order_by("-rating").select_related("category")[:5]

    categories = cache.get(CATEGORY_CACHE_KEY)
    if not categories:
        categories = list(Category.objects.all())
        cache.set(
            CATEGORY_CACHE_KEY, categories, CATEGOTY_CACHE_TTL
        )  # Кешуємо на 1 годину

    return render(
        request,
        "projects/home.html",
        {"categories": categories, "best_products": best_products},
    )


# CBV для списку категорій
class CategoryListView(ListView):
    model = Category
    template_name = "projects/category_list.html"
    context_object_name = "categories"


# CBV для перегляду однієї категорії та її продуктів
class CategoryDetailView(DetailView):
    model = Category
    template_name = "projects/category.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.products.all()
        return context


@ratelimit(key="ip", rate="100/m", method="GET", block=True)
def product_list(request):
    products = Product.objects.select_related("category").all()
    return render(request, "projects/product_list.html", {"products": products})


@ratelimit(key="ip", rate="100/m", method="GET", block=True)
def product_details(request, slug):
    product = get_object_or_404(Product.objects.select_related(), slug=slug)
    return render(request, "projects/product_details.html", {"product": product})


@ratelimit(key="ip", rate="100/m", method="GET", block=True)
def product_search(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    return render(
        request, "projects/product_search.html", {"query": query, "results": results}
    )
