from django.contrib import admin
from .models import MyCustomUserModel, UserAddress
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Register your models here.
admin.site.unregister(User)


class MyUserAdmin(UserAdmin):
    list_display = ['username', 'id', 'email', 'first_name', 'last_name', 'is_staff']


admin.site.register(User, MyUserAdmin)

admin.site.register(UserAddress)


@admin.register(MyCustomUserModel)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'email', 'phone_number', 'melli_code', 'profile_pic']

# @admin.register(CustomTokenModel)
# class CustomTokenModelAdmin(admin.ModelAdmin):
#     list_display = ['user', 'key']
