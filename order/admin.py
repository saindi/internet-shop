from django.contrib import admin
from order.models import OrderItemModel, OrderModel, CancellationModel


@admin.register(OrderModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = "id", "user", "created", "status"


@admin.register(OrderItemModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = "order", "product", "price", "quantity"

@admin.register(CancellationModel)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = "order",


