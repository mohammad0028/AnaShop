from django.urls import path
from .views import all_products_page, ProductsList, CategoryPage, product_detail

urlpatterns = [
    path('category-<slug>', CategoryPage.as_view()),
    path('products-fbv', all_products_page),
    path('products-cbv', ProductsList.as_view(), name='show_all_products'),
    path('product/<title>', product_detail),
]
