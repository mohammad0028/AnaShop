# Generated by Django 3.0.7 on 2020-08-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ana_account', '0020_auto_20200811_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomusermodel',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_imgs/'),
        ),
    ]
