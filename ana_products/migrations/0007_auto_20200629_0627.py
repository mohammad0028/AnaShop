# Generated by Django 3.0.7 on 2020-06-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_products', '0006_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
