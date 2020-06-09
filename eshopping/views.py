from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, ProfileForm, AddressForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from .models import Customer, Products, OrderItem, Orders, Address, Favorites
from django.utils import timezone
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def indexPage(request, ):
    items = Products.objects.all()

    context = {'items': items}
    return render(request, 'eshopping/index.html', context)

def search(request):
    if request.method == 'GET':
        Keywords = request.GET.get('Keywords')
        item = Products.objects.filter(product_name__icontains=Keywords)
        context = {'item': item, 'Keywords': Keywords}
        return render(request, 'eshopping/result.html', context)
    else:
        return redirect('home')


def result(request):
    context = {}
    return render(request, 'eshopping/result.html', context)
def aboutPage(request):
    context = {}
    return render(request, 'eshopping/about.html', context)

@unauthenticated_user
def authenticationPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'email or password incorrect')

    context = {}
    return render(request, 'eshopping/authentication.html', context)

def logoutUser(request):
    logout(request)
    return redirect('authenticate')

@unauthenticated_user
def signupPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )

            messages.success(request, 'Account was successfully created ')
            return redirect('authenticate')

    context = {'form': form}
    return render(request, 'eshopping/signup.html', context)

@login_required(login_url='authenticate')
def address_bookPage(request):
    show_address = Address.objects.filter(user=request.user.customer )

    context = {'show_address': show_address }
    return render(request, 'eshopping/address-book.html', context)


@login_required(login_url='authenticate')
def delete_address(request ):
    show_address = Address.objects.get(user=request.user.customer)
    show_address.delete()


    return redirect('address_book')


@login_required(login_url='authenticate')
def add_addressPage(request):
    initial_data ={
        'user': request.user.customer,
        'Addressname': "home",
        'office_box': "A00",
        'location': "home",
        'telephone': "0000"
    }
    show_address, created = Address.objects.get_or_create(user=request.user.customer )
    form = AddressForm(instance=show_address)

    if AddressForm(instance=show_address):
        if request.method == 'POST':
            form = AddressForm(request.POST, request.FILES, instance=show_address or None)
            if form.is_valid():
                form.save()
                return redirect('address_book')


    context = {'form': form,}
    return render(request, 'eshopping/add_address.html', context)



def account_recoveryPage(request):
    context = {}
    return render(request, 'eshopping/account-recovery.html', context)

@login_required(login_url='authenticate')
def checkoutPage(request):
    display_address = Address.objects.filter(user=request.user.customer)
    total_checkout = Orders.objects.filter(user=request.user.customer, ordered=False)

    context = {'display_address': display_address, 'total_checkout': total_checkout }
    return render(request, 'eshopping/checkout.html', context)

class OrderSummaryView(View):
    def get(self, *args, **kwargs):

        try:
            order = Orders.objects.get(user=self.request.user.customer, ordered=False)
            context = {'object': order}
            return render(self.request, 'eshopping/order_summary.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have an active order")
            return redirect('home')

@login_required(login_url='authenticate')
def couponsPage(request):
    context = {}
    return render(request, 'eshopping/coupons.html', context)


@login_required(login_url='authenticate')
def dashboardPage(request):
    context = {}
    return render(request, 'eshopping/dashboard.html', context)


@login_required(login_url='authenticate')
def favoritesPage(request):
    favorites = Favorites.objects.filter(user=request.user.customer, favorite=True)
    context = {'favorites': favorites}
    return render(request, 'eshopping/favourites.html', context)

def products_listPage(request):
    items =Products.objects.all()
    context = {'items':items}
    return render(request, 'eshopping/list-products.html', context)

@login_required(login_url='authenticate')
def ordersPage(request):
    context = {}
    return render(request, 'eshopping/oders.html', context)


@login_required(login_url='authenticate')
def personal_detilsPage(request):
    customer = request.user.customer
    form = ProfileForm(instance=customer)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'eshopping/personal-details.html', context)


def view_productPage(request, pk):
    view = get_object_or_404(Products, pk=pk)
    detail = Products.objects.filter(pk=pk)

    context = {'view': view, 'detail': detail}
    return render(request, 'eshopping/view-product.html', context)

@login_required(login_url='authenticate')
def select_addressPage(request):
    context = {}
    return render(request, 'eshopping/select-address.html', context)

@login_required(login_url='authenticate')
def specific_orderPage(request):
    context = {}
    return render(request, 'eshopping/specificOrders.html', context)


def add_to_cart(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user.customer,
        ordered=False)
    order_qs = Orders.objects.filter(user=request.user.customer, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity has been updated in cart')

        else:
            messages.info(request, 'This item has been added to the cart')
            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Orders.objects.create(user=request.user.customer, order_date=order_date)
        order.items.add(order_item)
        messages.info(request, 'This item has been added to the cart')

    return redirect('order_summary')

def remove_from_cart(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Orders.objects.filter(user=request.user.customer, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user.customer,
                ordered=False,
            )[0]
            order.items.remove(order_item)
            messages.info(request, 'This item has been removed from the cart')
            return redirect('home')
        else:
            messages.info(request, 'This item was not in  the cart')
            return redirect('home')
    else:
        messages.info(request, "You don't have an order")
        return redirect('order_summary')


def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Products, pk=pk)
    order_qs = Orders.objects.filter(user=request.user.customer, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user.customer,
                ordered=False,
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            order_item.save()
            messages.info(request, 'This item quantity has been reduced from the cart')
            return redirect('order_summary')
        else:
            messages.info(request, 'This item was not in  the cart')
            return redirect('home')
    else:
        messages.info(request, "You don't have an order")
        return redirect('home')

@login_required(login_url='authenticate')
def add_to_favourite(request, pk):
    favorite_item = get_object_or_404(Products, pk=pk)
    favs, created = Favorites.objects.get_or_create(
        user=request.user.customer,
        favorite_item=favorite_item,
        favorite=True,
    )
    favs.save()
    return redirect('favorites')


def delete_from_favourite(request, pk):
    favorite_item = get_object_or_404(Products, pk=pk)
    favs, created = Favorites.objects.get_or_create(
        favorite_item=favorite_item,
        user=request.user.customer,
        favorite=True,
    )
    if Favorites.objects.filter(user=request.user.customer, favorite=True).exists():
        favs.delete()

    return redirect('favorites')

def trialpage(request):

    context = {}
    return render(request, 'eshopping/trialpage.html', context)
