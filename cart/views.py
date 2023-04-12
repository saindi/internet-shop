from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import ProductModel
from cart.cart import Cart
from cart.forms import CartAddProductForm


@require_POST
def cart_add_view(request: HttpRequest, product_slug: str) -> HttpResponse:
    cart = Cart(request)
    product = get_object_or_404(ProductModel, slug=product_slug)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )

    return redirect('cart:detail')


def cart_remove_view(request: HttpRequest, product_slug: str) -> HttpResponse:
    cart = Cart(request)

    product = get_object_or_404(ProductModel, slug=product_slug)

    cart.remove(product)

    return redirect('cart:detail')


def cart_detail_view(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)

    return render(request, 'cart/detail.html', {'cart': cart})
