from django.shortcuts import render, redirect
from ana_products.models import Product
from .models import Cart, CartItem, Coupon, UsedCoupon
from iran_db.models import IranShahr, IranOstan


# Create your views here.


def shopping_cart(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    context = {}

    # for modal that says successfullyShoppingDone after paying and redirects user to this page(shopping_cart.html)
    # it has been setted at the end of shopping_cart function
    if 'successfullyShoppingDone' in request.session.keys():
        request.session.pop('successfullyShoppingDone')
        context['showModal'] = True
        context['message'] = 'کاربر گرامی خرید شما با موفقیت انجام شد.'

    current_user = request.user
    # to display CartItems of user
    user_shopping_cart = Cart.objects.filter(user=current_user, ordered=False).first()
    if user_shopping_cart:
        curr_user_orders = user_shopping_cart.products.all()

        # calculating total price of every product considering its quantity:
        for every in curr_user_orders:
            every.total_price = every.quantity * every.product.price
        context['orders'] = curr_user_orders

        # calculating total price of all products in shopping cart
        totalPriceOfAll = 0
        for every in curr_user_orders:
            totalPriceOfAll += every.total_price
        context['totalPriceOfAll'] = totalPriceOfAll

        # calculating tax (9%)
        tax = totalPriceOfAll * 0.09
        tax = int(tax)
        context['tax'] = tax

        # calculating final price of all products without considering discount coupons
        transport_cost = 10000
        global finalPrice
        finalPrice = totalPriceOfAll + tax + transport_cost
        context['finalPrice'] = finalPrice

        # sending list of provinces to province selection :
        provinces = IranOstan.objects.all()
        context['provinces'] = provinces

    else:
        context['noShoppingCartForThisUser'] = True

    # to increase quantity of a product in shopping cart
    if request.GET.get('addQuantity'):
        # 1. increase quantity of CartItem
        product_id = request.GET.get('addQuantity')
        product = Product.objects.filter(id=product_id).first()
        myTemp = CartItem.objects.get(user=current_user, product=product, ordered=False)
        myTemp.quantity += 1
        myTemp.save()
        return redirect(request.path)

    # to decrease quantity of a product in shopping cart
    elif request.GET.get('subtractQuantity'):
        product_id = request.GET.get('subtractQuantity')
        product = Product.objects.filter(id=product_id).first()
        myTemp = CartItem.objects.get(user=current_user, product=product, ordered=False)
        if myTemp.quantity > 1:
            myTemp.quantity -= 1
            myTemp.save()
            return redirect(request.path)

    # to delete a product from shopping cart
    elif request.GET.get('deleteOrder'):
        order_id = request.GET.get('deleteOrder')
        CartItem.objects.filter(id=order_id).delete()
        cartOfCurrentUser = Cart.objects.filter(user=current_user, ordered=False)
        if cartOfCurrentUser[0].products.count() == 0:
            cartOfCurrentUser.delete()
        return redirect(request.path)

    if request.method == "POST":
        theFormName = request.POST.get('hidden_input_form_name')
        # this form is for submitting the discount coupon :
        if theFormName == 'discountForm':
            enteredCouponCode = request.POST.get('coupon_code')
            matchCouponCode = Coupon.objects.filter(code=enteredCouponCode, expired=False).first()
            alreadyUserUsed = UsedCoupon.objects.filter(user=request.user, coupon=matchCouponCode).first()
            if matchCouponCode and not alreadyUserUsed:
                # set usedCouponId in session in order to access it if user submits payingForm after
                # submitting discountForm (it is used in get_paid_price() function at the bottom of this page)
                request.session['usedCoupon'] = matchCouponCode.id
                discount = matchCouponCode.discount_price
                discountFinalPrice = finalPrice - discount
                context['discountFinalPrice'] = discountFinalPrice
            else:
                context['showModal'] = True
                context['message'] = 'کد تخفیف معتبر نیست یا قبلا استفاده کرده اید.'


        # this form is for paying the shopping cart :
        elif theFormName == 'payingForm':
            # getting final paid price by using following function :
            paidPrice = get_paid_price(request)
            paidPrice = paidPrice.replace(',', '')
            paidPrice = int(paidPrice)
            # setting paidPrice as current Cart model`s total_price and set its ordered=True
            userCartModel = Cart.objects.filter(user=current_user, ordered=False)
            allCartItems = userCartModel.first().products.all()
            userCartModel.update(total_price=paidPrice)
            userCartModel.update(ordered=True)

            # get the CartItems in user_shopping_cart and set their ordered=True :
            for order in allCartItems:
                order.ordered = True
                order.save()

            # show a modal that says shopping is done successfully :
            # it is used at the beginning of shopping_cart() function
            request.session['successfullyShoppingDone'] = 'successfullyDone'

            return redirect(request.path)

    return render(request, 'shopping_cart.html', context)


def get_paid_price(request):
    # if user pays with discount coupon :
    if request.POST.get('discount_price'):
        finalPaidPriceWithDiscountCoupon = request.POST.get('discount_price')
        # here I get the used coupon id from session which I manually setted in session earlier :
        usedCoupon_id = request.session.pop('usedCoupon')
        usedCoupon = Coupon.objects.filter(id=usedCoupon_id).first()
        # creating an object from UsedCoupon model and set its user and coupon fields :
        usedCoupon_obj = UsedCoupon()
        usedCoupon_obj.user = request.user
        usedCoupon_obj.coupon = usedCoupon
        usedCoupon_obj.save()

        return finalPaidPriceWithDiscountCoupon

    # if user pays without discount coupon :
    else:
        finalPaidPriceWithOutDiscountCoupon = request.POST.get('final_price')
        return finalPaidPriceWithOutDiscountCoupon
