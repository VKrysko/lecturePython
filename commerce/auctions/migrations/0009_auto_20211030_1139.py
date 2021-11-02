# Generated by Django 3.2.8 on 2021-10-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20211030_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='product',
            name='winner',
        ),
        migrations.AddField(
            model_name='bid',
            name='date_bid',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
