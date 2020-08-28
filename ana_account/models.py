from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import User
from django.db import models
# import os
# from django.conf import settings
# import binascii


# Create your models here.


class MyCustomUserModel(User):
    profile_pic = models.ImageField(upload_to='profile_imgs/', default='profile_imgs/default.png', blank=True)
    melli_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'


# users address
class UserAddress(models.Model):
    user = models.ForeignKey(MyCustomUserModel, default=None, on_delete=models.CASCADE, related_name='address')
    user_address = models.CharField(max_length=150, null=True)


'''
# model manager for CustomTokenModel
class CustomTokenModelManager(models.Manager):
    def get_user_token(self, user):
        token = self.get_queryset().get(user=user)
        return token


class CustomTokenModel(models.Model):
    """
    An access token that is associated with a user.  This is essentially the same as the token model from Django REST Framework
    """
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="token", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    objects = CustomTokenModelManager()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(CustomTokenModel, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
'''
