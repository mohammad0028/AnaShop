# Generated by Django 3.0.7 on 2020-08-11 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0025_auto_20200811_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomusermodel',
            name='melli_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
