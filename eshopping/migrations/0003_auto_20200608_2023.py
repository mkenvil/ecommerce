# Generated by Django 3.0.4 on 2020-06-08 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopping', '0002_auto_20200608_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Out On Delivery', 'Out On Delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Phone Accessories', 'Phone Accessories'), ('Laptop Accessories', 'Laptop Accessories'), ('Laptops', 'Laptops'), ('Phones', 'Phones')], default='Phones', max_length=150),
        ),
    ]
