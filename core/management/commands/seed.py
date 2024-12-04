import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Category, Product, Order


class Command(BaseCommand):
    help = "Generate fixture data for Category, Product, and Order models with realistic values"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to generate fixture data with real values...")

        # Categories
        category_names = [
            "Electronics", "Books", "Clothing", "Home Appliances", "Toys"
        ]
        categories = []
        for name in category_names:
            category = Category.objects.create(
                name=name,
                slug=name.lower().replace(" ", "-")
            )
            categories.append(category)
        self.stdout.write(f"Created {len(categories)} categories.")

        # Products
        product_data = [
            {"name": "Smartphone", "description": "Latest smartphone with high-end features", "price": 699.99, "stock": 50},
            {"name": "Laptop", "description": "Powerful laptop for professionals", "price": 1199.99, "stock": 30},
            {"name": "Bluetooth Headphones", "description": "Noise-cancelling wireless headphones", "price": 199.99, "stock": 100},
            {"name": "Microwave Oven", "description": "Compact microwave oven for quick meals", "price": 89.99, "stock": 20},
            {"name": "Children's Toy Car", "description": "Durable and colorful toy car for kids", "price": 29.99, "stock": 200},
            {"name": "Fiction Novel", "description": "Bestselling fiction novel", "price": 15.99, "stock": 150},
            {"name": "T-shirt", "description": "Comfortable and stylish cotton T-shirt", "price": 12.99, "stock": 300},
            {"name": "Refrigerator", "description": "Energy-efficient refrigerator", "price": 599.99, "stock": 10},
            {"name": "Action Figure", "description": "Collectible action figure for fans", "price": 49.99, "stock": 80},
            {"name": "Cookbook", "description": "Cookbook with easy and healthy recipes", "price": 25.99, "stock": 100},
        ]
        products = []
        for data in product_data:
            product = Product.objects.create(
                name=data["name"],
                description=data["description"],
                price=data["price"],
                stock=data["stock"],
                category=random.choice(categories)
            )
            products.append(product)
        self.stdout.write(f"Created {len(products)} products.")

        # Users for orders
        users = []
        for i in range(1, 6):
            user = User.objects.create_user(
                username=f"user{i}",
                email=f"user{i}@example.com",
                password="password123"
            )
            users.append(user)
        self.stdout.write(f"Created {len(users)} users.")

        # Orders
        statuses = ['order_placed', 'order_confirmed', 'order_dispatched', 'order_delivered', 'order_canceled']
        for i in range(20):
            Order.objects.create(
                user=random.choice(users),
                product=random.choice(products),
                quantity=random.randint(1, 5),
                status=random.choice(statuses)
            )
        self.stdout.write("Created 20 orders with realistic values.")

        self.stdout.write(self.style.SUCCESS("Fixture data generation completed!"))
