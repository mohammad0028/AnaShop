from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ana_account.models import MyCustomUserModel, UserAddress
from ana_cart.models import Cart
from .forms import ChangePasswordForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage


# Create your views here.


def profile_page(request):
    if request.user.is_authenticated:

        # this user is the one which is located in users model at auth (admin panel)
        current_user_id = request.user.id
        # this user is the one which is located in MyCustomUserModel at ana_profile app(created by developer not auth)
        current_user = MyCustomUserModel.objects.filter(id=current_user_id)
        current_user = current_user.first()

        # user addresses :
        addresses = UserAddress.objects.filter(user=current_user)

        # user shopping cart (paid and unpaid)
        shoppingCarts = Cart.objects.filter(user=current_user).order_by('-order_at')

        context = {
            'current_user': current_user,
            'addresses': addresses,
            'shoppingCarts': shoppingCarts

        }

        return render(request, 'profile_page.html', context)


    else:
        return redirect('/login')


# def change_password(request):
#     if not request.user.is_authenticated:
#         return redirect('/login')
#
#     # this user is the one which is located in users model at auth (admin panel)
#     current_user_id = request.user.id
#     # this user in the one which is located in MyCustomUserModel at ana_profile app(created by developer)
#     current_user = MyCustomUserModel.objects.filter(id=current_user_id)
#     current_user = current_user.first()
#
#     change_password_form = ChangePasswordForm(request.POST or None, user=request.user)
#
#     context = {
#         'current_user': current_user,
#         'change_password_form': change_password_form
#     }
#
#     if change_password_form.is_valid():
#         new_password = change_password_form.cleaned_data.get('new_password')
#         new_password = make_password(new_password)
#         MyCustomUserModel.objects.filter(id=current_user_id).update(password=new_password)
#         myuser = MyCustomUserModel.objects.filter(id=current_user_id).first()
#         # request.user.set_password(new_password)
#         update_session_auth_hash(request, myuser)
#         return redirect('profile')
#
#     return render(request, 'change_password.html', context)


# def set_my_cookie(request):
#     response = HttpResponse('mammad')
#     response.set_cookie('cookie_name', 'cookie_value')

# temp = AbstractBaseUser()
# temp.set_password()


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    current_user_id = request.user.id
    current_user = MyCustomUserModel.objects.filter(id=current_user_id)
    current_user = current_user.first()
    change_password_form = ChangePasswordForm(request.POST or None, user=request.user)

    if change_password_form.is_valid():

        new_password = change_password_form.cleaned_data.get('new_password')
        new_password = make_password(new_password)

        my_user = MyCustomUserModel.objects.get(id=current_user_id)
        my_user.password = new_password
        my_user.save()

        the_user = User.objects.filter(id=current_user_id).first()
        update_session_auth_hash(request, the_user)  # Important!

        context = {
            'current_user': current_user,
        }

        return render(request, 'profile_page.html', context)

    else:
        context = {
            'current_user': current_user,
            'change_password_form': change_password_form
        }
        return render(request, 'change_password.html', context)


def edit_personal_info(request):
    current_user_id = request.user.id
    current_user = MyCustomUserModel.objects.filter(id=current_user_id).first()
    context = {
        'current_user': current_user,
    }

    if request.method == 'POST':
        theFormName = request.POST.get('hidden_input_form_name')
        # if change profile picture form is submitted:
        if theFormName == 'editAvatarForm' and request.FILES.get('profilePic'):
            img = request.FILES['profilePic']
            cur_user = MyCustomUserModel.objects.get(id=current_user_id)
            if cur_user.profile_pic != 'profile_imgs/default.png':
                cur_user.profile_pic.delete()
            cur_user.profile_pic = img
            cur_user.save()
            return redirect(request.path)
        # if other user info form submitted :
        elif theFormName == 'userInfoForm':
            user_name = request.POST.get('userName')
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')
            email = request.POST.get('email')
            melli_code = request.POST.get('melliCode')
            phone_number = request.POST.get('phoneNumber')

            cur_user = MyCustomUserModel.objects.get(id=current_user_id)
            cur_user.username = user_name
            cur_user.first_name = first_name
            cur_user.last_name = last_name
            cur_user.email = email
            cur_user.melli_code = melli_code
            cur_user.phone_number = phone_number
            cur_user.save()
            return redirect('profile')

    return render(request, 'edit_info.html', context)
