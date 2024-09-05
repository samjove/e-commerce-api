import stripe
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem, Product
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated


stripe.api_key = settings.STRIPE_SECRET_KEY
domain = settings.DOMAIN


class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Cart.objects.get(user=self.request.user)


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    # User submits product id and quantity.
    # View creates cart and cart item objects if they don't exist and adds product to cart.
    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product, quantity=quantity
        )
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()
        return Response(
            {"status": "item added to cart"}, status=status.HTTP_201_CREATED
        )


class RemoveFromCartView(generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        cart = Cart.objects.get(user=request.user)
        CartItem.objects.filter(cart=cart, product_id=product_id).delete()
        return Response(
            {"status": "item removed from cart"}, status=status.HTTP_204_NO_CONTENT
        )


class CheckoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    # Submits cart items as line items to create a Stripe checkout session.
    # On success, responds with a checkout session id that the frontend should then use to fetch the Stripe checkout page.
    def post(self, request, *args, **kwargs):
        user = request.user
        cart_items = CartItem.objects.filter(cart__user=user)
        if not cart_items.exists():
            return Response(
                {"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST
            )
        line_items = []
        for item in cart_items:
            line_items.append(
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": item.product.title,
                        },
                        "unit_amount": int(item.product.price * 100),
                    },
                    "quantity": item.quantity,
                }
            )

        try:
            session = stripe.checkout.Session.create(
                line_items=line_items,
                mode="payment",
                success_url=domain + "/success/",
                cancel_url=domain + "/cancel/",
            )

            return Response({"session_id": session.id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def success_view(request):
    pass


def cancel_view(request):
    pass
