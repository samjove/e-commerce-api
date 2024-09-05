from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path("", CartView.as_view(), name="cart_detail"),
    path("add/", AddToCartView.as_view(), name="add_to_cart"),
    path("remove/", RemoveFromCartView.as_view(), name="remove_from_cart"),
]
