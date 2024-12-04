import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Category, Product, Order


@pytest.fixture
def test_user():
    User = get_user_model()
    user = User.objects.create_user(username='testuser', password='password')
    return user


@pytest.fixture
def test_product(test_user):
    category = Category.objects.create(name='Test Category',
                                       slug='test-category')
    product = Product.objects.create(
        name='Test Product',
        description='This is a test product',
        price=10.00,
        stock=100,
        category=category,

    )
    return product


@pytest.mark.django_db
@pytest.mark.parametrize(
    'status, transition, expected_status',
    [
        ('order_placed', 'confirm_order', 'order_confirmed'),
        ('order_confirmed', 'dispatch_order', 'order_dispatched'),
        ('order_dispatched', 'deliver_order', 'order_delivered'),
        ('order_placed', 'deliver_order', None),
    ],
)
def test_order_status_transition_flow(test_user, test_product, status, transition,
                                 expected_status):
    order = Order.objects.create(
        user=test_user,
        product=test_product,
        quantity=1,
        status=status,
    )
    getattr(order, transition)()
    if expected_status:
        assert order.status == expected_status
    else:
        with pytest.raises(AttributeError):
            getattr(order, transition)()


@pytest.mark.parametrize('initial_status, target_status', [
    ('order_placed', 'order_canceled'),
    ('order_confirmed', 'order_canceled'),
    ('order_dispatched', 'order_canceled'),  # Invalid transition
])
@pytest.mark.django_db
def test_order_status_transition_cancel(test_user, test_product, initial_status,
                                 target_status):
    order = Order.objects.create(
        user=test_user,
        product=test_product,
        quantity=1,
        status=initial_status,
    )
    if initial_status == 'order_placed' and target_status == 'order_canceled':
        order.cancel_order()
    elif initial_status == 'order_confirmed' and target_status == 'order_canceled':
        order.cancel_order()
    elif initial_status == 'order_dispatched' and target_status == 'order_canceled':
        with pytest.raises(Exception) as exc_info:
            order.cancel_order()
        assert str(
            exc_info.value) == 'Invalid transition from order_dispatched to order_canceled'
    else:
        with pytest.raises(Exception) as exc_info:
            order.cancel_order()
        assert str(
            exc_info.value) == 'Invalid transition from order_placed to order_canceled'
    assert order.status == target_status


@pytest.mark.parametrize('initial_status, target_status', [
    ('order_canceled', 'order_placed'),
    ('order_canceled', 'order_confirmed'),
])
@pytest.mark.django_db
def test_undo_cancel_order(test_user, test_product, initial_status, target_status):
    order = Order.objects.create(
        user=test_user,
        product=test_product,
        quantity=1,
        status=initial_status,
    )
    order.undo_cancel_order()
    assert order.status == initial_status

