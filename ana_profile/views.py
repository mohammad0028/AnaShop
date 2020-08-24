from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ana_account.models import MyCustomUserModel
from .forms import ChangePasswordForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser


# Create your views here.


def profile_page(request):
    # print(f'profile: {request.user}')
    # print(request.session.session_key)
    # print(f'profile page :{request.COOKIES.items()}')
    # mytoken = request.COOKIES['csrftoken']
    # myuser = MyCustomUserModel.objects.filter(csrftoken=mytoken)
    # print(myuser)
    # value = request.COOKIES.get('cookie_name')
    # if value is not None:
    # print(request.session.items())
    # print(request.COOKIES.items())

    if request.user.is_authenticated:

        # this user is the one which is located in users model at auth (admin panel)
        current_user_id = request.user.id
        # this user in the one which is located in MyCustomUserModel at ana_profile app(created by developer not auth)
        current_user = MyCustomUserModel.objects.filter(id=current_user_id)
        current_user = current_user.first()

        context = {
            'current_user': current_user
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
