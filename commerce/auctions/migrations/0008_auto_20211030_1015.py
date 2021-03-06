# Generated by Django 3.2.8 on 2021-10-30 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20211030_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='products')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('description', models.TextField(blank=True)),
                ('starting_bid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='auctions.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopper', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_item', to='auctions.product')),
                ('user_watchlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_watchlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_comment', to='auctions.product')),
                ('user_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['url', 'id', 'name'], name='auctions_ca_url_25f7d8_idx'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddField(
            model_name='bid',
            name='item_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_bid', to='auctions.product'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user_bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['url', 'id', 'name'], name='auctions_pr_url_f60c39_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='name_products_idx'),
        ),
    ]
