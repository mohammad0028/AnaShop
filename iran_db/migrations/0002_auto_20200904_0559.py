# Generated by Django 3.1 on 2020-09-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iran_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iranshahr',
            name='ostan',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
