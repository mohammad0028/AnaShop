from django.urls import path
from ana_profile.views import profile_page, change_password, edit_personal_info

urlpatterns = [
    path('profile', profile_page, name='profile'),
    path('change-password', change_password, name='change-password'),
    path('edit-info', edit_personal_info, name='edit-info'),

]
