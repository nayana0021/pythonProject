from django.urls import path

from .views import cart

app_name = "payment"

urlpatterns = [
    # http://127.0.0.1:8000/payment/cart
    path("cart/", cart, name="cart")
]
