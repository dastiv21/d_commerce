from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('order_placed', 'Order Placed'),
        ('order_confirmed', 'Order Confirmed'),
        ('order_dispatched', 'Order Dispatched'),
        ('order_delivered', 'Order Delivered'),
        ('order_canceled', 'Order Canceled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_lenght=40, choices=STATUS_CHOICES, default='order_placed')

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def order_price(self):
        return self.product.price * self.quantity

    # @transition(field=status, source='order_placed', target='order_confirmed')
    # def confirm_order(self):
    #     """Transition to confirm the order."""
    #     pass
    #
    # @transition(field=status, source='order_confirmed',
    #             target='order_dispatched')
    # def dispatch_order(self):
    #     """Transition to dispatch the order."""
    #     pass
    #
    # @transition(field=status, source='order_dispatched',
    #             target='order_delivered')
    # def deliver_order(self):
    #     """Transition to mark the order as delivered."""
    #     pass

    # @transition(field=status, source=['order_placed', 'order_confirmed'],
    #             target='order_canceled')
    # def cancel_order(self):
    #     """Transition to cancel the order."""
    #     pass
    #
    # @transition(field=status, source='order_canceled', target='order_canceled')
    # def undo_cancel_order(self):
    #     """Transition to undo the cancellation of the order."""
    #     pass

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def cart_item_price(self):
        return self.product.price * self.quantity

class external_service():
    confirm_pickup = True


class MockExternalService:
    @staticmethod
    def confirm_pickup(order):
        """
        Simulates the external service's confirm_pickup function.

        Args:
            order (Order): The order object to process.

        Returns:
            bool: True if the order was successfully confirmed for pickup, False otherwise.
        """
        if not order or order.status != 'order_confirmed':
            return False  # Fail if the order is not in the correct state
        # Simulate updating the order in the external system
        print(f"Processing order {order.id} for pickup.")
        return True  # Simulate a successful operation