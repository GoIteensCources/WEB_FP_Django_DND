from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
	path('', views.home, name='home'),
	path('categories/', views.CategoryListView.as_view(), name='categories_list'),
	path('categories/<str:slug>/', views.CategoryDetailView.as_view(), name='category'),
	path('products/', views.product_list, name='product_list'),
	path('products/<str:slug>/', views.product_details, name='product_details'),
	path('search/', views.product_search, name='search'),
]
