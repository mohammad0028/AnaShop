# Generated by Django 3.0.7 on 2020-08-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0028_auto_20200811_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomusermodel',
            name='melli_code',
            field=models.CharField(blank=True, default=' ', max_length=10),
        ),
        migrations.AddField(
            model_name='mycustomusermodel',
            name='phone_number',
            field=models.CharField(blank=True, default=' ', max_length=11),
        ),
    ]
