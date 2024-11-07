from django.urls import path, include

from core.views import ProductListView, ProductCreateView, LoginView, \
    AllOrderListView

urlpatterns = [

    path('login', LoginView.as_view(), name='login'),
    path('product-list', ProductListView.as_view(), name='product_list'),
    path('all-orders', AllOrderListView.as_view(), name='order_list'),
    path('product-create', ProductCreateView.as_view(), name='product_create'),
    ]