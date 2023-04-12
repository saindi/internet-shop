from rest_framework import routers

from api import views

app_name = 'api'


user_router = routers.SimpleRouter()

order_item_router = routers.SimpleRouter()
order_router = routers.SimpleRouter()
cancellation_router = routers.SimpleRouter()

product_router = routers.SimpleRouter()
category_router = routers.SimpleRouter()


user_router.register('user', views.UserViewSet, basename="user")
user_router.register('order-item', views.OrderItemViewSet, basename="order_item")
user_router.register('order', views.OrderViewSet, basename="order")
user_router.register('cancellation', views.CancellationViewSet, basename="cancellation")
user_router.register('product', views.ProductViewSet, basename="product")
user_router.register('category', views.CategoryViewSet, basename="category")


__all__ = ['user_router', 'order_item_router', 'order_router', 'cancellation_router']