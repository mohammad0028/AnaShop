# Generated by Django 3.1 on 2020-08-26 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='order_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]