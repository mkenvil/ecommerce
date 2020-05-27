from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Favorites)
admin.site.register(Checkout)
admin.site.register(OrderItem)
admin.site.register(Address)

