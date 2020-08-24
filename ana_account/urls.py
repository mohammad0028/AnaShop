from django.conf.urls import url
from django.urls import path
from .views import (
    login_user,
    register_user,
    logout_user,
    MyPasswordResetView,
    MyPasswordResetConfirmView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register_user, name='register'),
    path('logout', logout_user, name='logout'),

    # the following urls and ClassBaseView s are for forgot-password :

    # url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/$', MyPasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
