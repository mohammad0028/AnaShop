# Generated by Django 3.0.7 on 2020-06-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_products', '0005_auto_20200628_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
