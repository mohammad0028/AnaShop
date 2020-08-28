from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from ana_cart.models import CartItem, Cart
from ana_products.models import Product


# Create your views here.


class SearchProductsView(ListView):
    template_name = 'search_products.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is None or len(query) == 0:
            return Product.objects.get_active_products()
        elif query is not None:
            return Product.objects.search(query)
        else:
            return Product.objects.get_active_products()

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(SearchProductsView, self).get_context_data(*args, **kwargs)
        # this is for when user searches sth
        context['search'] = self.request.GET.get('q')
        if self.request.GET.get('addToCart'):
            if self.request.user.is_authenticated:
                context['showModal'] = True
                addToCartProductId = self.request.GET.get('addToCart')
                context['product_id'] = int(addToCartProductId)
                addToCartProduct = get_object_or_404(Product, id=addToCartProductId)
                current_user = self.request.user
                cartItemMatch = CartItem.objects.filter(product=addToCartProduct, user=current_user, ordered=False)
                # if current user has a CartItem for this product(already has this product in his cart shopping):
                if cartItemMatch.exists() and cartItemMatch.count() == 1:
                    context['modalMessage'] = 'این محصول قبلا به سبد خرید شما اضافه شده است.'
                # else if user does not have this product already in cartItem model :
                else:
                    context['modalMessage'] = 'این محصول با موفقیت به سبد خرید شما اضافه شد.'
                    cartMatch = Cart.objects.filter(user=current_user, ordered=False)
                    # if there is Cart model for this user:
                    # 1.create CartItem 2.add CartItem to Cart.products
                    if cartMatch.exists():
                        cartMatch = cartMatch.first()
                        cartItem_obj = CartItem.objects.create(user=current_user, product=addToCartProduct)
                        cartMatch.products.add(cartItem_obj)

                    else:
                        # if there is no Cart model for this user:
                        # 1.create CartItem 2.create Cart 3.add CartItem to Cart.products
                        cartItem_obj = CartItem.objects.create(user=current_user, product=addToCartProduct)
                        cart_obj = Cart.objects.create(user=current_user)
                        cart_obj.products.add(cartItem_obj)
            else:
                context['showModal'] = True
                context['modalMessage'] = 'کاربر گرامی ، برای افزودن محصول به سبد خرید ابتدا وارد سایت شوید.'
                context['product_id'] = int(self.request.GET.get('addToCart'))

        return context
