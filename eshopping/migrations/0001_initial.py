# Generated by Django 3.0.4 on 2020-05-16 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='usericon.png', null=True, upload_to='')),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('Addressname', models.CharField(max_length=50, null=True)),
                ('office_box', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('telephone', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Laptop Accessories', 'Laptop Accessories'), ('Phones', 'Phones'), ('Laptops', 'Laptops'), ('Phone Accessories', 'Phone Accessories')], default='Phones', max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000000, null=True)),
                ('display_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('view_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(max_length=500, null=True)),
                ('shipping_details', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Out On Delivery', 'Out On Delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=150)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
                ('expected_date', models.DateTimeField(null=True)),
                ('items', models.ManyToManyField(to='eshopping.OrderItem')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Products')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Customer')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshopping.Products'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Customer'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Customer')),
                ('favorite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Products')),
            ],
            options={
                'verbose_name_plural': 'Favorites',
            },
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Products')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshopping.Customer')),
            ],
            options={
                'verbose_name_plural': 'Checkout',
            },
        ),
    ]