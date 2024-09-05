from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, CheckoutView, success_view, cancel_view

urlpatterns = [
    path("", CartView.as_view(), name="cart_detail"),
    path("add/", AddToCartView.as_view(), name="add_to_cart"),
    path("remove/", RemoveFromCartView.as_view(), name="remove_from_cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("success/", success_view, name="success" ),
    path("cancel/", cancel_view, name="cancel"),
]
