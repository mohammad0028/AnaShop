from django import forms
from ana_account.models import MyCustomUserModel


# from django.db.models.loading import cache


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور فعلی'})
    )

    new_password = forms.CharField(
        label='کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور جدید'})
    )
    re_new_password = forms.CharField(
        label='تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار کلمه عبور جدید'})
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        valid = self.user.check_password(self.cleaned_data['current_password'])
        if not valid:
            raise forms.ValidationError("کلمه عبور فعلی اشتباه است.")
        return valid

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')

        def use_one_digit(user_password):
            digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(len(digits)):
                if str(i) in user_password:
                    return False
            return True

        if len(new_password) < 5:
            raise forms.ValidationError('حداقل طول کلمه عبور 5 کاراکتر میباشد')
        elif use_one_digit(new_password):
            raise forms.ValidationError('حداقل از یک عدد در کلمه عبور استفاده نمایید')

        return new_password

    def clean_re_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        re_new_password = self.cleaned_data.get('re_new_password')
        if new_password is not None and new_password != re_new_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند')

        return new_password
