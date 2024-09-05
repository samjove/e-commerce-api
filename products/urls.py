from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="product_list_create"),
    path(
        "<int:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="product_detail"
    ),
]
