from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from order.models import OrderItemModel, OrderModel, CancellationModel
from cart.cart import Cart

from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings


@login_required
def order_create_view(request):
    cart = Cart(request)

    if len(cart) == 0:
        return HttpResponseRedirect(reverse_lazy('cart:detail'))

    if cart.get_total_price() > request.user.money:
        # Очистка корзины
        cart.clear()

        return render(request, 'order/no_money.html')

    # Проверка количества товара
    for item in cart:
        if item["quantity"] > item["product"].amount:
            # Очистка корзины
            cart.clear()

            return render(request, 'order/no_product_amount.html')

    # Уменьшение количество купленного товара
    for item in cart:
        item["product"].amount -= item["quantity"]
        item["product"].save()

    order = OrderModel.objects.create(
        user=request.user,
        status=1
    )

    for item in cart:
        OrderItemModel.objects.create(
            order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
        )

    # Снимает деньги
    request.user.money -= cart.get_total_price()
    request.user.save()

    # Очистка корзины
    cart.clear()

    return HttpResponseRedirect(reverse_lazy('user:profile_url'))


@staff_member_required(login_url=settings.LOGIN_URL)
def cancellation_list_view(request: HttpRequest) -> HttpResponse:
    context = {"cancellations": CancellationModel.objects.all()}

    return render(request, 'order/cancellation_list.html', context)


@login_required
def cancellation_create_view(request: HttpRequest, order_id: int) -> HttpResponse:
    try:
        order = OrderModel.objects.get(id=order_id)
    except OrderModel.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('user:profile_url'))

    order.status = 4
    order.save()

    CancellationModel.objects.create(
        order=order,
        status=1
    )

    return HttpResponseRedirect(reverse_lazy('user:profile_url'))


@staff_member_required(login_url=settings.LOGIN_URL)
def cancellation_confirm_view(request: HttpRequest, cancellation_id: int) -> HttpResponse:
    try:
        cancellation = CancellationModel.objects.get(id=cancellation_id)
    except CancellationModel.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('order:cancellations_list'))

    cancellation.order.user.money += cancellation.order.get_total_cost()
    cancellation.order.user.save()

    cancellation.order.status = 3
    cancellation.order.save()

    for order_item in OrderItemModel.objects.filter(order=cancellation.order):
        order_item.product.amount += order_item.quantity
        order_item.product.save()

    cancellation.status = 2
    cancellation.save()

    return HttpResponseRedirect(reverse_lazy('order:cancellations_list'))


@staff_member_required(login_url=settings.LOGIN_URL)
def cancellation_cancel_view(request: HttpRequest, cancellation_id: int) -> HttpResponse:
    try:
        cancellation = CancellationModel.objects.get(id=cancellation_id)
    except CancellationModel.DoesNotExist:
        return HttpResponseRedirect(reverse_lazy('order:cancellations_list'))

    cancellation.order.status = 1
    cancellation.order.save()

    cancellation.delete()

    return HttpResponseRedirect(reverse_lazy('order:cancellations_list'))
