# Generated by Django 3.1 on 2020-08-30 16:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ana_cart', '0006_couponused'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CouponUsed',
            new_name='UsedCoupon',
        ),
    ]