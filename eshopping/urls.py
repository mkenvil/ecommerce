from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.indexPage, name='home'),
    path('search/', views.search, name='search'),
    path('result/', views.result, name='result'),
    path('checkout/', views.checkoutPage, name='checkout'),
    path('coupons/', views.couponsPage, name='coupons'),
    path('dashboard/', views.dashboardPage, name='dashboard'),
    path('favorites/', views.favoritesPage, name='favorites'),
    path('product_list', views.products_listPage, name='product_list'),
    path('orders/', views.ordersPage, name='orders'),
    path('personal_details', views.personal_detilsPage, name='personal_details'),
    path('select_address/', views.select_addressPage, name='select_address'),
    path('specific_order/', views.specific_orderPage, name='specific_order'),
    path('view_product/<int:pk>/', views.view_productPage, name='view_product'),
    path('authenticate/', views.authenticationPage, name='authenticate'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup', views.signupPage, name='signup'),
    path('account_recovery/', views.account_recoveryPage, name='account_recovery'),
    path('address_book/', views.address_bookPage, name='address_book'),
    path('add_address', views.add_addressPage, name='add_address'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('order_summary/', views.OrderSummaryView.as_view(), name='order_summary'),
    path('remove_single_item_from_cart/<int:pk>/', views.remove_single_item_from_cart,
         name='remove_single_item_from_cart'),
    path('delete_address/', views.delete_address, name='delete_address'),
    path('add_to_favourite/<int:pk>', views.add_to_favourite, name='add_to_favourite'),
    path('delete_from_favourite/<int:pk>', views.delete_from_favourite, name='delete_from_favourite'),

    path('trialpage', views.trialpage, name='trialpage')
]