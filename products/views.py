from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


def home(request):
	categories = Category.objects.all()
	best_products = Product.objects.order_by('-rating')[:5]
	return render(request, 'projects/home.html', {'categories': categories, 'best_products': best_products})


# CBV для списку категорій
class CategoryListView(ListView):
	model = Category
	template_name = 'projects/category_list.html'
	context_object_name = 'categories'


# CBV для перегляду однієї категорії та її продуктів
class CategoryDetailView(DetailView):
	model = Category
	template_name = 'projects/category.html'
	context_object_name = 'category'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['products'] = self.object.products.all()
		return context


def product_list(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'projects/product_list.html', {'products': products})


def product_details(request, slug):
    product = get_object_or_404(Product.objects.select_related('category'), slug=slug)
    return render(request, 'projects/product_details.html', {'product': product})


def product_search(request):
	query = request.GET.get('q', '')
	results = []
	if query:
		results = Product.objects.filter(
			Q(name__icontains=query) | Q(description__icontains=query)
		)
	return render(request, 'projects/product_search.html', {'query': query, 'results': results})
