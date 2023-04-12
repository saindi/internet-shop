from rest_framework import serializers
from order.models import OrderModel, OrderItemModel, CancellationModel


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"


class CancellationSerializers(serializers.ModelSerializer):
    class Meta:
        model = CancellationModel
        fields = "__all__"
