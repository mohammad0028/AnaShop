from django.urls import path
from ana_profile.views import profile_page,change_password

urlpatterns = [
    path('profile', profile_page, name='profile'),
    path('change-password', change_password, name='change-password'),

]
