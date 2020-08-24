# Generated by Django 3.0.7 on 2020-07-16 09:23

import ana_products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_products', '0012_auto_20200710_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ana_products.models.upload_image_path),
        ),
    ]
