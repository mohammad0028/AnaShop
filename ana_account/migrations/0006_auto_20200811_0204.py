# Generated by Django 3.0.7 on 2020-08-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0005_useraddress_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomusermodel',
            name='melli_code',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='mycustomusermodel',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
