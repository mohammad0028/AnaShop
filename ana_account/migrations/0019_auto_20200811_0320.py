# Generated by Django 3.0.7 on 2020-08-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0018_auto_20200811_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomusermodel',
            name='melli_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mycustomusermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
