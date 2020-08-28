from django.contrib import admin
from ana_cart.models import CartItem, Cart


# Register your models here.

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'ordered']


admin.site.register(CartItem, CartItemAdmin)


class CartAdmin(admin.ModelAdmin):
    fields = ['user', 'products', 'ordered']
    list_display = ['user', 'get_list_of_products', 'ordered']

    def get_list_of_products(self, obj):
        return " - \n".join([str(p.product) for p in obj.products.all()])

    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
