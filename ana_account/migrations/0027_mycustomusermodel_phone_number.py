# Generated by Django 3.0.7 on 2020-08-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0026_mycustomusermodel_melli_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomusermodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
