from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'}),
        label='کلمه عبور'
    )


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
        label='نام کاربری',
        # validators=[
        #     validators.MaxLengthValidator(limit_value=20,
        #                                   message='تعداد کاراکترهای وارد شده نمیتواند از 20 بیشتر باشد'),
        #     validators.MinLengthValidator(limit_value=4, message='تعداد کاراکترهای وارد شده نمیتواند از 4 کمتر باشد')
        # ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        label='ایمیل'
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور'})
    )
    re_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور'})
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        queryset = User.objects.filter(username=user_name)
        if queryset.exists():
            raise forms.ValidationError('این کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        queryset = User.objects.filter(email=email)

        if "@yahoo.com" not in email and "@gmail.com" not in email:
            raise forms.ValidationError('ایمیل خود را به صورت صحیح وارد نمایید')

        elif queryset.exists():
            raise forms.ValidationError('کاربر قبلا با این ایمیل ثبت نام کرده است')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        def use_one_digit(user_password):
            digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(len(digits)):
                if str(i) in user_password:
                    return False
            return True

        if len(password) < 5:
            raise forms.ValidationError('حداقل طول کلمه عبور 5 کاراکتر میباشد')
        elif use_one_digit(password):
            raise forms.ValidationError('حداقل از یک عدد در کلمه عبور استفاده نمایید')

        return password

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password is not None and password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return password


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="ایمیل",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'placeholder': 'ایمیل را وارد کنید'})
    )

