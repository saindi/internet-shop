from rest_framework.viewsets import ModelViewSet

from catalog.models import ProductModel, CategoryModel
from catalog.serialiers import ProductSerializers, CategorySerializers
from order.models import OrderItemModel, OrderModel, CancellationModel
from order.serialiers import OrderItemSerializers, OrderSerializers, CancellationSerializers
from user.models import UserModel
from user.serialiers import UserSerializers

from api.permissions import UserOwnerOrStaffPermission

from rest_framework import permissions


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializers
    queryset = ProductModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializers
    queryset = CategoryModel.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializers
    queryset = OrderItemModel.objects.all()
    permission_classes = permissions.IsAuthenticated, [permissions.IsAdminUser]


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializers
    queryset = OrderModel.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class CancellationViewSet(ModelViewSet):
    serializer_class = CancellationSerializers
    queryset = CancellationModel.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializers
    queryset = UserModel.objects.all()
    permission_classes = [permissions.IsAuthenticated, UserOwnerOrStaffPermission]
