# Generated by Django 3.0.4 on 2020-06-08 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorites',
            options={'verbose_name_plural': 'Favorite'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Addressname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='office_box',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
        migrations.AddField(
            model_name='favorites',
            name='favorite_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshopping.Products'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshopping.Customer'),
        ),
        migrations.AddField(
            model_name='products',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10000000),
        ),
        migrations.AddField(
            model_name='products',
            name='shipping_charge',
            field=models.DecimalField(decimal_places=2, max_digits=10000000, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='vat',
            field=models.DecimalField(decimal_places=2, max_digits=10000000, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='usericon.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out On Delivery', 'Out On Delivery'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Phones', 'Phones'), ('Phone Accessories', 'Phone Accessories'), ('Laptop Accessories', 'Laptop Accessories'), ('Laptops', 'Laptops')], default='Phones', max_length=150),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(default='Unknown', max_length=200)),
                ('seller_category', models.CharField(max_length=150, null=True)),
                ('seller_contact', models.IntegerField(blank=True, null=True)),
                ('seller_email', models.EmailField(max_length=254, null=True)),
                ('seller_location', models.CharField(max_length=200, null=True)),
                ('seller_description', models.TextField(null=True)),
                ('seller_product', models.ManyToManyField(to='eshopping.Products')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Seller',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Addressname', models.CharField(default='home', max_length=50)),
                ('office_box', models.CharField(default='home', max_length=50)),
                ('location', models.CharField(default='home', max_length=100)),
                ('telephone', models.IntegerField(default='000')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshopping.Customer')),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
    ]
