# Generated by Django 3.0.7 on 2020-08-11 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0030_auto_20200811_0451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycustomusermodel',
            name='melli_code',
        ),
        migrations.RemoveField(
            model_name='mycustomusermodel',
            name='phone_number',
        ),
    ]
