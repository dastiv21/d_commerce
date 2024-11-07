from decimal import Decimal

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import OrderItem, Order, Product
from core.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_list():
    client = APIClient()
    url = reverse('product_list')
    response = client.get(url)
    assert response.status_code == 200

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Fixture to set up an instance of APIClient
@pytest.fixture
def api_client():
    return APIClient()

# Fixture to create an admin user
@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

# Fixture to create a client user
@pytest.fixture
def client_user(db):
    return User.objects.create_user('client', 'client@example.com', 'clientpass')

# Test access with admin permission
@pytest.mark.django_db
def test_all_order_list_view_admin(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    url = '/all-orders'  # Replace with your actual URL to the AllOrderListView
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test access with client permission (should not have access)
@pytest.mark.django_db
def test_all_order_list_view_client(api_client, client_user):
    api_client.force_authenticate(user=client_user)
    url = '/all-orders'  # Replace with your actual URL to the AllOrderListView
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN

# Test access without authentication
@pytest.mark.django_db
def test_all_order_list_view_no_auth(api_client):
    url = '/all-orders'  # Replace with your actual URL to the AllOrderListView
    response = api_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN