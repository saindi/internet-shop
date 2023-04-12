from django.urls import path

from api import routers
from api import auth


app_name = "api"

urlpatterns = [
    path("auth/", auth.ObtainauthTokenView.as_view(), name="api-token"),

    *routers.user_router.urls,

    *routers.order_item_router.urls,
    *routers.order_router.urls,
    *routers.cancellation_router.urls,

    *routers.product_router.urls,
    *routers.category_router.urls,
]
