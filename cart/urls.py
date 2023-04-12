from django.urls import path
from cart import views

app_name = "cart"

urlpatterns = [
    path('cart/', views.cart_detail_view, name='detail'),
    path('cart/add/<slug:product_slug>/', views.cart_add_view, name='add'),
    path('cart/remove/<slug:product_slug>/', views.cart_remove_view, name='remove'),
]