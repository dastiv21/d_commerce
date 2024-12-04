from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ProductListView, ProductCreateView, LoginView, \
    RegisterView, ShoppingCartView, register, OrderViewSet, home

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')


urlpatterns = [

    path('', home, name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('product-list', ProductListView.as_view(), name='product_list'),
    path('product-create', ProductCreateView.as_view(), name='product_create'),
    path('register', RegisterView.as_view(), name='register'),
    path('register', register, name='register'),
    path('cart', ShoppingCartView.as_view(), name='shopping_cart'),
    path('', include(router.urls)),

    # Explicitly define custom action routes for state transitions
    path('orders/<int:pk>/confirm_order/', OrderViewSet.as_view({'post': 'confirm_order'}), name='confirm_order'),
    path('orders/<int:pk>/dispatch_order/', OrderViewSet.as_view({'post': 'dispatch_order'}), name='dispatch_order'),
    path('orders/<int:pk>/deliver_order/', OrderViewSet.as_view({'post': 'deliver_order'}), name='deliver_order'),
    path('orders/<int:pk>/cancel_order/', OrderViewSet.as_view({'post': 'cancel_order'}), name='cancel_order'),
    path('orders/<int:pk>/undo_cancel_order/', OrderViewSet.as_view({'post': 'undo_cancel_order'}), name='undo_cancel_order'),
]
