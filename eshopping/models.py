from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(default='usericon.png',height_field=None, width_field=None, max_length=100, blank=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name_plural = 'Customer'

    def __str__(self):
        return str(self.user)

    def get_address_book_url(self):
        return reverse('address_book', kwargs={'pk': self.pk})


class Products(models.Model):
    CATEGORY = {
        ('Phones', 'Phones'),
        ('Phone Accessories', 'Phone Accessories'),
        ('Laptops', 'Laptops'),
        ('Laptop Accessories', 'Laptop Accessories'),
    }
    product_name = models.CharField(max_length=200, null=True)
    category = models.CharField(choices=CATEGORY, default='Phones', max_length=150)
    price = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    discount_price = models.DecimalField(max_digits=10000000, decimal_places=2, default=0, blank=True)
    display_image = models.ImageField(height_field=None, width_field=None, max_length=100, null=True, blank=True)
    view_image = models.ImageField(height_field=None, width_field=None, max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, blank=False, null=True)
    shipping_details = models.CharField(max_length=200, null=True)
    shipping_charge = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)
    vat = models.DecimalField(max_digits=10000000, decimal_places=2, null=True)



    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'pk': self.pk})

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'pk': self.pk})

    def get_remove_from_cart_url(self):
        return reverse('remove_from_cart', kwargs={'pk': self.pk})

    def get_remove_single_item_from_cart_url(self):
        return reverse('remove_single_item_from_cart', kwargs={'pk': self.pk})

    def get_add_to_favourite_url(self):
        return reverse('add_to_favourite', kwargs={'pk': self.pk})

    def get_delete_from_favourite_url(self):
        return reverse('delete_from_favourite', kwargs={'pk': self.pk})


class Favorites(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    favorite = models.BooleanField(default=False)
    favorite_item = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    #favorite_item = models.ManyToManyField(Products)

    class Meta:
        verbose_name_plural = "Favorite"

    def __str__(self):
        return str(self.user)



class OrderItem(models.Model):
    user = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.product_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def get_shipping_price(self):
        return self.item.shipping_charge

    def get_vat_price(self):
        return self.item.vat

    def get_add_expenses(self):
        return self.item.shipping_charge + self.item.vat

    def get_checkout_price(self):
        return self.get_final_price() + self.get_add_expenses()



class Orders(models.Model):
    STATUS = {
        ('Pending', 'Pending'),
        ('Out On Delivery', 'Out On Delivery'),
        ('Delivered', 'Delivered'),
    }
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=STATUS, max_length=150, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True,)
    ordered = models.BooleanField(default=False,)
    expected_date = models.DateTimeField(auto_now=False, null=True)
    items = models.ManyToManyField(OrderItem)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.user}"

    def get_total_amount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

    def get_total_shipping(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_shipping_price()
        return total

    def get_total_vat(self):
        vat = 0
        for order_item in self.items.all():
            vat += order_item.get_vat_price()
        return vat

    def get_total_checkout_amount(self):
        total_amount = 0
        for order_item in self.items.all():
            total_amount += order_item.get_checkout_price()
        return total_amount


class Address(models.Model):
    user = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    Addressname = models.CharField(max_length=50, default='home')
    office_box = models.CharField(max_length=50, default='home')
    location = models.CharField(max_length=100, default='home')
    telephone = models.IntegerField(default='000')


    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return str(self.Addressname)



class Checkout(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    cart = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Checkout'

    def __str__(self):
        return self.customer.customer_name


class Seller(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=200, default='Unknown', blank=False)
    seller_category = models.CharField(max_length=150, null=True)
    seller_contact = models.IntegerField(null=True, blank=True)
    seller_email = models.EmailField(null=True)
    seller_location = models.CharField(max_length=200, null=True)
    seller_description = models.TextField(null=True)
    seller_product = models.ManyToManyField(Products)

    class Meta:
        verbose_name_plural = 'Seller'

    def __str__(self):
        return str(self.seller_name)




