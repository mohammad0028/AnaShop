# Generated by Django 3.0.7 on 2020-08-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_products', '0017_auto_20200811_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
