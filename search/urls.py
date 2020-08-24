from django.urls import path
from .views import SearchProductsView

urlpatterns = [
    path('products/search', SearchProductsView.as_view()),
]
