from django.conf.urls import url
from django.urls import path
from .views import shopping_cart


urlpatterns = [
    path('shopping-cart', shopping_cart, name='shopping-cart')

]