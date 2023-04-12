from django.urls import path
from order import views

app_name = "order"

urlpatterns = [
    path('order/create/', views.order_create_view, name='create'),
    path('order/cancellations/', views.cancellation_list_view, name='cancellations_list'),
    path('order/cancellation/create/<int:order_id>', views.cancellation_create_view, name='cancellation_create'),
    path('order/cancellation/confirm/<int:cancellation_id>', views.cancellation_confirm_view, name='cancellation_confirm'),
    path('order/cancellation/cancel/<int:cancellation_id>', views.cancellation_cancel_view, name='cancellation_cancel'),
]