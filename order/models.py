from django.db import models
from catalog.models import ProductModel
from user.models import UserModel
import datetime


ORDER_STATUS = [
    (1, "Прийнятий"),
    (2, "Виконаний"),
    (3, "Скасовано"),
    (4, "Повернення"),
]

CANCELLATION_STATUS = [
    (1, "Не відпрацьовано"),
    (2, "Повернено"),
]


def date_now():
    return datetime.datetime.now()


class OrderModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        default=date_now
    )

    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return 'Order №{}'.format(self.id)

    def get_total_cost(self):
        return int(sum(item.get_cost() for item in self.items.all()))


class OrderItemModel(models.Model):
    order = models.ForeignKey(
        OrderModel,
        related_name='items',
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        ProductModel,
        related_name='order_items',
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.product)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = "Товары заказа"
        verbose_name_plural = "Товары заказов"
        ordering = ["id"]


class CancellationModel(models.Model):
    order = models.ForeignKey(
        OrderModel,
        related_name='order',
        on_delete=models.CASCADE
    )

    status = models.PositiveSmallIntegerField(choices=CANCELLATION_STATUS)

    class Meta:
        verbose_name = "Отмена"
        verbose_name_plural = "Отмены"
        ordering = ["id"]
