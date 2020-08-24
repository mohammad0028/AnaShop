from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordContextMixin
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django import forms
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm
from django.contrib.auth import authenticate, logout, password_validation
from django.contrib.auth.forms import SetPasswordForm
from .models import MyCustomUserModel
from django.contrib.auth import login


# -----------------------------------------------------------------------------------------------


# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        current_user = authenticate(request, password=password, username=user_name)
        if current_user is not None:
            # CustomTokenModel.objects.create(user=current_user)
            login(request, current_user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'نام کاربری یا کلمه عبور اشتباه است')

    context = {
        'login_form': login_form
    }

    return render(request, "account/login.html", context)


# -----------------------------------------------------------------------------------------------


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    context = {
        'register_form': register_form
    }
    if register_form.is_valid():
        username = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        MyCustomUserModel.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')

    return render(request, "account/register.html", context)


# ------------------------------------------------------------------------------------------------


def logout_user(request):
    # current_user = request.user
    # CustomTokenModel.objects.filter(user=current_user).delete()
    logout(request)
    return redirect('/')


# ------------------------------------------------------------------------------------------------


# this class inherits from builtin PasswordResetView class in view builtin module
# but with one little change : form_class should be like my customized form in forms.py
# this classBaseView is used in urls.py
class MyPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm


# ------------------------------------------------------------------------------------------------


class MySetPasswordForm(SetPasswordForm, forms.Form):
    error_messages = {
        'password_mismatch': 'کلمه عبور و تکرار آن یکسان نیستند.'
    }
    new_password1 = forms.CharField(
        label="کلمه عبور جدید :",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label="تکرار کلمه عبور جدید :",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )


class MyPasswordResetConfirmView(PasswordResetConfirmView, PasswordContextMixin, FormView):
    form_class = MySetPasswordForm
