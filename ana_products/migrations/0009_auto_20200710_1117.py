# Generated by Django 3.0.7 on 2020-07-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_products', '0008_auto_20200630_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
