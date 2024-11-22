from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import Product, Order, ShoppingCart
from core.serializers import ProductSerializer, UserSerializer, \
    OrderSerializer, RegisterSerializer, ShoppingCartSerializer
from core.utils import IsAdminOrReadOnly


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        user = User.objects.get(username=request.data['username'])
        return Response({
            'access': serializer.validated_data['access'],
            'refresh': serializer.validated_data['refresh'],
            'user': UserSerializer(user).data
        })

class ProductListView(APIView):
    """
    Retrieve a list of all products in the cloud storage.

    Returns:
        A JSON response with a list of all products and their details.

    Example response:

        [
            {
                "id": 1,
                "name": "Smartphone",
                "description": "Latest model with advanced features",
                "price": 699.99,
                "category": "Electronics"
            },
            ...
        ]
    """

    def get(self, request):
        products = Product.objects.prefetch_related('images').all()
        serializer = ProductSerializer(products, many=True,
                                       context={'request': request})
        return Response(serializer.data)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


class ProductCreateView(APIView):
    def post(self, request):
        # Create an instance of the serializer with the request data
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            # Save the new product to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return validation errors if any
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class AllOrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminOrReadOnly]


api_view(['GET'])
@permission_classes([IsAdminOrReadOnly])
def product_list(request):
    # Your logic to list products
    pass
    # return Response(product_data)

# views.py

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppingCartView(APIView):
    def get(self, request):
        try:
            shopping_cart = ShoppingCart.objects.get(user=request.user)
            serializer = ShoppingCartSerializer(shopping_cart)
            return Response(serializer.data)
        except ShoppingCart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ShoppingCartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
