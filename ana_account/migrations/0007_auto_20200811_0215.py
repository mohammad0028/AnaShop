# Generated by Django 3.0.7 on 2020-08-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0006_auto_20200811_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomusermodel',
            name='melli_code',
            field=models.BigIntegerField(max_length=10, null=True),
        ),
    ]
