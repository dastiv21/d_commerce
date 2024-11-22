from django.urls import path, include

from core.views import ProductListView, ProductCreateView, LoginView, \
    AllOrderListView, RegisterView, ShoppingCartView, register

urlpatterns = [

    path('login', LoginView.as_view(), name='login'),
    path('product-list', ProductListView.as_view(), name='product_list'),
    path('all-orders', AllOrderListView.as_view(), name='order_list'),
    path('product-create', ProductCreateView.as_view(), name='product_create'),

    # path('register', RegisterView.as_view(), name='register'),
    path('register', register, name='register'),
    path('cart', ShoppingCartView.as_view(), name='shopping_cart'),
]
